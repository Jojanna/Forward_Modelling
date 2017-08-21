__author__ = 'wallisj'
import numpy as np
import math

def reflectivity(ai1, ai2):
    r = (ai2 - ai1) / (ai2 + ai1)
    return r

def shuey_two(vp1, vp2, vs1, vs2, rho1, rho2):
    vp_mean = ((vp2+vp1)/2)
    vs_mean = ((vs2+vs1)/2)
    rho_mean = ((rho2+rho1)/2)
    g = 0.5 * (vp2 - vp1)/vp_mean - 2 * pow(vs_mean,2)/pow(vp_mean,2) * ((rho2-rho1)/rho_mean + 2 * (vs2-vs1)/vs_mean)
    r0 = 0.5 * ((vp2-vp1)/vp_mean + (rho2-rho1)/rho_mean)

    return r0, g

def shuey_three (vp1, vp2, vs1, vs2, rho1, rho2):
    vp_mean = ((vp2+vp1)/2)
    vs_mean = ((vs2+vs1)/2)
    rho_mean = ((rho2+rho1)/2)
    g = 0.5 * (vp2 - vp1)/vp_mean - 2 * pow(vs_mean,2)/pow(vp_mean,2) * ((rho2-rho1)/rho_mean + 2 * (vs2-vs1)/vs_mean)
    r0 = 0.5 * ((vp2-vp1)/vp_mean + (rho2-rho1)/rho_mean)
    f = 0.5 * (vp2 - vp1)/vp_mean

    return r0, g, f

def shuey_three_log (vp, vs, rho, depth):

    length = len(vp)

    i = 0
    r0_log = []
    g_log = []
    f_log = []
    z_mid = []

    while i < length-1:
        vp_mean = ((vp[i]+vp[i+1])/2)
        vs_mean = ((vs[i]+vs[i+1])/2)
        rho_mean = ((rho[i]+rho[i+1])/2)
        depth_mean = ((depth[i]+depth[i+1])/2)
        g = 0.5 * (vp[i+1] - vp[i])/vp_mean - 2 * pow(vs_mean,2)/pow(vp_mean,2) * ((rho[i+1]-rho[i])/rho_mean + 2 * (vs[i+1]-vs[i])/vs_mean)
        r0 = 0.5 * ((vp[i+1]-vp[i])/vp_mean + (rho[i+1]-rho[i])/rho_mean)
        f = 0.5 * (vp[i+1] - vp[i])/vp_mean

        z_mid.append(depth_mean)
        g_log.append(g)
        r0_log.append(r0)
        f_log.append(f)

        i = i+1

    return r0_log, g_log, f_log, z_mid

def elastic_impedance(vp, vs, rho, theta):

    ei = []
    for vp, vs, rho in zip(vp, vs, rho):
        k = (vs / vp) ** 2
        a = (1 + (math.sin(theta)) ** 2)
        b = -8 * k * (math.sin(theta)) ** 2
        c = 1 - 4 * k * (math.sin(theta)) ** 2

        e = vp ** a * vs **b * rho **c
        ei.append(e)

    return ei

def reflectivity(imp):
    length = len(imp)
    #print (length)
    i = 0
    r_log = [0] * (length-1)
    imp = np.array(imp)

    while i < length-1:
        r = (imp[i+1] - imp[i])/(imp[i+1] + imp[i])
        r_log[i] = r

        i = i+1
    #print (len(r_log))
    return r_log

def mid_depth(depth):
    length = len(depth)
    i = 0
    z_mid = []
    while i < length-1:
        depth_mean = ((depth[i]+depth[i+1])/2)
        z_mid.append(depth_mean)
        i = i+ 1

    return z_mid

#def attenuation(wavelet,)