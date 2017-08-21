__author__ = 'wallisj'

import numpy as np
import math

def depth_conversion(vp, depth, replacement_velocity):
    vp = list(vp)
    depth = list(depth)
    start_depth = depth[0]

    #print(vp)
    ti = []
    zmid = []
    n = len(vp)
    i = 0
    vi = []
    dz = []
    #print (n)
    ti.append(0)
    start_time = start_depth/replacement_velocity

    while i < (n-1):

        d = (depth[i+1] - depth[i])
        dz.append(d)
        t = d / vp[i]
        ti.append(t)
        zmid.append((depth[i+1] + depth[i])/2)
        v = vp[i] ** 2 * d
        vi.append(v)
        i = i + 1
    #print (ti)
    owt_s = []

    j = 0
    while j < len(ti):
        if j == 0:
            tj = ti[0] + start_time
        else:
            tj = sum(ti[0:j+1]) + start_time
        owt_s.append(tj)
        j = j + 1

    #print (time)
    vavg = []
    owt_ms = []
    twt_ms = []

    for d, t in zip(zmid, owt_s):
        if t == 0:
            v = replacement_velocity
        else:
            v = np.array(d)/np.array(t)
        vavg.append(v)
        owt_ms.append(t*1000)
        twt_ms.append(t*2000)

    #print(twt_ms)
    #print(vavg)


    return twt_ms, owt_ms, vavg, zmid