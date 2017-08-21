__author__ = 'wallisj'

import numpy as np
import matplotlib.pyplot as plt
import math


# calculate moduli

#from C1_DataFilter import (vs,rho,vp)

def calc_moduli(vp, vs, rho):
    rho = rho * 1000
    AI = rho * vp
    mu = (pow(vs,2) * rho)
    k = (pow(vp,2) * rho - 4/3 * mu)
    ratio = vp / vs
    return k, mu, AI, ratio, rho

def variables (properties):
    #phiT = properties[0]
    k = properties[1]
    mu = properties[2]
    rho = properties[3]
    vp = np.power((k + 4/3 * mu)/(rho), 0.5)
    vs = np.power((mu / rho), 0.5)
    AI = rho * vp
    ratio = vp/vs

    return vp, vs, AI, ratio

