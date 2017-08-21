__author__ = 'wallisj'

import numpy as np
import matplotlib.pyplot as plt
from Agile_wavelets import ormsby

length = 0.512
dt = 0.001
f = 5 # A low wavelength of 5 Hz

def ricker(f, length, dt): #f = dominant freq, length = trace length?, dt = sample interval?
    t = np.linspace(-length/2, (length-dt)/2, length/dt) #t = time elapsed
    y = (1.0 - 2.0*(np.pi**2)*(f**2)*(t**2)) * np.exp(-(np.pi**2)*(f**2)*(t**2)) # y = amplitude
    return t, y
"""
#t = ricker(f, length, dt)[0]
#y = ricker(f, length, dt)[1]
t, y = ricker(f, length, dt)

fig = plt.plot(t, y)
plt.show(fig)
"""

f_ormsby = (5,10,40,60) #f_lc, f_lp, f_hp, f_hc

"""
def ormsby (f_ormsby, length, dt):
    f_lc = f_ormsby[0]
    f_lp = f_ormsby[1]
    f_hp = f_ormsby[2]
    f_hc = f_ormsby[3]
    t = np.linspace(-length/2, (length-dt)/2, length/dt)
    #for t in tn:
    #a = np.array(np.pi * f_lp * t)
    y = -((np.pi * f_hc)**2/(np.pi * (f_hc - f_hp)) - (np.pi * f_hp) ** 2 / (np.pi * (f_hc - f_hp)) - (np.pi * f_lp) ** 2 / (np.pi * (f_lp - f_lc)) * np.sinc(np.array(np.pi * f_lp * t)) - (np.pi * f_lc) ** 2 / (np.pi * (f_lp - f_lc)) * (np.sinc(np.array(np.pi * f_lc * t))) ** 2)

    return t, y
"""


t1, y1 = ormsby(length, dt, f_ormsby)
fig1 = plt.plot(t1, y1)
plt.show(fig1)

#print ()