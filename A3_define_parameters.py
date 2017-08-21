__author__ = 'wallisj'

from Agile_wavelets import ricker, ormsby
from A4_load_stat_wavelet import wavelet_load
import matplotlib.pyplot as plt
from A1_load_database import data_load


filepath = r'C:\Users\joanna.wallis\Documents\GU17-301-Zennor-Forties\Python\mean_properties\23_16b-9\GOR\23_16b-9_database.txt'
output_path = r'C:\Users\joanna.wallis\Documents\GU17-301-Zennor-Forties\Python\mean_properties\23_16b-9\GOR\forward_modelling'
header_lines = 1
folder = 'scenarios'
folder_lists = 'lists'
folder_interfaces = ''
ricker_freq = 25
ormsby_freq = (5,10,40,60)
#wavelet_path = r'/data/TZA/python/wallisj/Python/1D_Scenario_Modelling/wavelets/ormsby1.txt'
#wavelet = ricker(0.512, 0.001, ricker_freq) # ricker wavelet: ricker(duration, dt, f)
wavelet = ormsby(0.512, 0.001, ormsby_freq)# t1, y1 = ormsby(length, dt, ormsby_freq)
replacement_velocity = 2000 # required for depth conversion if start depth =/= 0

#wavelet_stat = wavelet_load(wavelet_path)
#for t,a in wavelet_stat:
    #wavelet_dt = t[1] - t[0] # wavelet sample rate in seconds

"""
t, a = wavelet_load(wavelet_path)
fig1 = plt.plot(t,a)
plt.show(fig1)
"""
#wavelet = wavelet_stat
database = data_load(filepath, header_lines)
#print (database)

#n = len(database)
n = 4
layers = 2
thickness = (3, 5) # thickness in m
log_interval = 0.8 # log interval in m
start_depth = 0