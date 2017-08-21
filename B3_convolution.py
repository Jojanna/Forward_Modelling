__author__ = 'wallisj'

import numpy as np
import math
from scipy import signal
from A2_define_model import create_logs
#from A1_load_database import data_load
from C3_shuey import shuey_three_log, elastic_impedance, reflectivity, mid_depth
from A3_define_parameters import database, replacement_velocity, wavelet,output_path, folder, folder_lists, folder_interfaces, n, layers, thickness, log_interval, start_depth #wavelet_dt,
from C2_Calculate_Moduli import calc_moduli

from C5_depth_conversion import depth_conversion
# log convolution - 1D models

#output = np.array(create_logs(database, n, layers, thickness, log_interval, start_depth))


#database = data_load(filepath)


def convolution(database, layers, thickness, log_interval, start_depth, wavelet):
    all_models = np.array(create_logs(database, layers, thickness, log_interval, start_depth))

    no_models = len(all_models)
    #print (no_models)
    #print (all_models[0])

    #print (all_models)
    # specify wavelet for convolution
    wavelet_A = wavelet
    # length to pad signal with for convolution
    wavelet_time = [float(t) for t in (wavelet_A[0])]
    pad = (max(wavelet_time))
    # print(pad)
    dt = (wavelet_time[1] - wavelet_time[0])
    #print(dt)
    # create list of angles for calculation of elastic impedance
    #theta = list(range(5, 50, 5))
    theta = (25, 30)
    #print (theta)

    ai_all = []
    g_all = []
    r0_all = []
    f_all =[]
    ei_all = []
    rx_all = []
    zmid_all = []
    vavg_all = []
    twt_ms_all = []
    owt_ms_all = []
    all_gathers = []


    for model in all_models:
        model = model.T
        code = model[0]
        depth = [float(j) for j in (model[1])]
        vp = [float(j) for j in (model[2])]
        vs = [float(j) for j in (model[3])]
        rho = [float(j) for j in (model[4])]
        ephi = [float(j) for j in (model[5])]
        vsh = [float(j) for j in (model[6])]
        sw = [float(j) for j in (model[7])]

        #print (vp)
        #print (type(vp))
        """
        refs = shuey_three_log(vp,vs,rho,depth)
        #print (refs)
        r0_log = refs[0]
        g_log = refs[1]
        f_log = refs[2]
        zmid = refs[3]
        """

        # depth convert and find mid depths - corresponds with depth of reflection
        output = depth_conversion(vp,depth, replacement_velocity)
        twt_ms = output[0]
        twt_ms_all.append(twt_ms)
        owt_ms = output[1]
        owt_ms_all.append(owt_ms)
        vavg = output[2]
        vavg_all.append(vavg)
        zmid = output[3]
        zmid_all.append(zmid)
        #print (list(pad))
        #print(max(twt_ms))





        #print (len(list(owt_ms_round)))
        # calculate extended elastic impedance for all angles in range
        ei = []
        rx = []
        angle_gather = []
        angle_gather_amp = []
        #zmid = []

        for t in theta: # for all angles
        #for vp, vs, rho in (zip(vp,vs,rho)):
            e = elastic_impedance(vp, vs, rho, t) #find logs for each angle
            ei.append(e) #append all angles for each model
            r = reflectivity(e)
            #print (r)
            rx.append(r)

            signal_length = max(owt_ms) + 2 * pad
            no_samples = math.ceil(signal_length / dt)
            time = [float(t) for t in np.arange(start = -1 * pad,stop = no_samples*dt-pad,step = dt)]
            signal = [float(n) for n in list([0] * no_samples)]
            #print (len(time))
            #print (len(signal))
            signal_dict = (dict(zip(time,signal)))
            #signal_dictionary = dict((zip(signal, time)))#dict(zip(signal, time))
            #print (len(signal_dict))

            #r_series = list(zip(owt_ms_round, r))

            owt_ms_round = []

            for t in owt_ms:
                owt_ms_round.append(dt * round(float(t/dt),0))

            for owt_ms_round,r in (zip(owt_ms_round, r)):
                #print (owt_ms_round)

                if (float(r)) != 0:
                    rep = owt_ms_round
                    #print(rep,r)
                    for t in signal_dict.keys():
                        if t == rep:
                            signal_dict[t] = r
            traces = []
            signal_time = []
            signal_amp = []
            for t in sorted(signal_dict):
                signal_time.append(t)
                signal_amp.append(signal_dict[t])
                a = (t,signal_dict[t])
                traces.append(a)
            print (traces)

            angle_gather.append(traces)
            angle_gather_amp.append(signal_amp)

            # convolve traces



            for angle in angle_gather_amp:
                r0_conv = signal.convolve(wavelet_A, signal_amp)
            #print
            #print (signal_dict)
        all_gathers.append(angle_gather)
        ei_all.append(ei) #append all models
        rx_all.append(rx)
        #print (ei)
        """
        # find mid depths - corresponds with depth of reflection
        zmid = mid_depth(depth)
        zmid_all.append(zmid)
        """




        #print (time)
        #print (len(time))
        #print (len(signal))

        #print (owt_ms)
        #print (owt_ms_round)




        """

        """
        #print (r_series)





        #print (output)


        #moduli = calc_moduli(vp, vs, rho)
        #ai_model = moduli[0]

        #ai_all.append(ai_model)



    #print (ei_all)
    #print (ai_all[0])


convolution(database, layers, thickness, log_interval, start_depth, wavelet)
#print (output)


"""
vp1 = vp[i]
vp2 = vp[i+1]
vs1 = vs[i]
vs2 = vs[i+1]
rho1 = rho[i]
rho2 = rho[i+1]
ephi1 = ephi[i]
ephi2 = ephi[i+1]
"""

