__author__ = 'wallisj'
from A1_load_database import data_load
import numpy as np
from itertools import product
import os


from A3_define_parameters import filepath, output_path, folder, folder_lists, folder_interfaces, n, layers, thickness, log_interval, start_depth
#print (int_thickness)

#database = data_load(filepath)

#print(vp_list)

def all_interfaces(database):
    n = len(database)
    database = database.T
    scenario_list = database[0]
    vp_list = database[1]
    vs_list = database[2]
    rho_list = database[3]
    ephi_list = database[4]
    vsh_list = database[5]
    sw_list = database[6]

    layers = 2

    grid = list(product(range(n),repeat = layers))
    #print (grid)
    scenario_no = 1
    all_interfaces_list = []

    for iteration in grid:
        scenario_log = []
        vp_log = []
        vs_log = []
        rho_log = []
        ephi_log = []
        vsh_log = []
        sw_log = []

        i = 0

        while i < layers:
            position = iteration[i] # i = layer number, position = which facies in database
            scenario_log.append(scenario_list[position])
            vp_log.append(vp_list[position])
            vs_log.append(vs_list[position])
            rho_log.append(rho_list[position])
            ephi_log.append(ephi_list[position])
            vsh_log.append(vsh_list[position])
            sw_log.append(sw_list[position])
            i = i + 1

        vp_log = [float(j) for j in (np.hstack(vp_log))]
        vs_log = [float(j) for j in (np.hstack(vs_log))]
        rho_log = [float(j) for j in (np.hstack(rho_log))]
        ephi_log = [float(j) for j in (np.hstack(ephi_log))]
        vsh_log = [float(j) for j in (np.hstack(vsh_log))]
        sw_log = [float (j) for j in (np.hstack(sw_log))]
        scenario_log = np.hstack(scenario_log)

        zipped = list(zip(scenario_log,vp_log,vs_log, rho_log, ephi_log, vsh_log, sw_log))
        all_interfaces_list.append(zipped)

        if not os.path.exists(os.path.join(output_path,folder_interfaces)):
            os.makedirs(os.path.join(output_path,folder_interfaces))
    #print (code_log)
        scenario_log = list(scenario_log)
        filename = str(scenario_no)+'_'+('_'.join(map(str,scenario_log)))
    #print (filename)
        file = open(output_path+folder_interfaces+'/'+filename+'.txt','w')
        file.write("code \t vp \t vs \t rho \t ephi \t vsh \t sw \n")
        for entry in zipped:
        #file.write("%f \n" % entry)
            file.write("%s \t %f \t %f \t %f \t %f \t %f \t %f \n" % entry)
        scenario_no = scenario_no + 1

    return all_interfaces_list


print ()


def create_lists(database, layers):
    n = len(database)
    database = database.T
    code_list = database[0]
    vp_list = database[2]
    vs_list = database[3]
    rho_list = database[4]
    ephi_list = database[5]
    vsh_list = database[6]
    sw_list = database[7]

    grid = list(product(range(n),repeat = layers))
    scenario_no = 1
    all_models_list = []

    for iteration in grid:
        code_log = []
        vp_log = []
        vs_log = []
        rho_log = []
        ephi_log = []
        vsh_log = []
        sw_log = []

        l = len(iteration) # n = total number of layers
        i = 0

        while i < l:
            position = iteration[i] # i = layer number, position = which facies in database
            code_log.append(code_list[position])
            vp_log.append(vp_list[position])
            vs_log.append(vs_list[position])
            rho_log.append(rho_list[position])
            ephi_log.append(ephi_list[position])
            vsh_log.append(vsh_list[position])
            sw_log.append(sw_list[position])
            i = i + 1

        vp_log = [float(j) for j in (np.hstack(vp_log))]
        vs_log = [float(j) for j in (np.hstack(vs_log))]
        rho_log = [float(j) for j in (np.hstack(rho_log))]
        ephi_log = [float(j) for j in (np.hstack(ephi_log))]
        vsh_log = [float(j) for j in (np.hstack(vsh_log))]
        sw_log = [float (j) for j in (np.hstack(sw_log))]
        code_log = np.hstack(code_log)

        zipped = list(zip(code_log,vp_log,vs_log, rho_log, ephi_log, vsh_log, sw_log))
        all_models_list.append(zipped)

        if not os.path.exists(os.path.join(output_path,folder_lists)):
            os.makedirs(os.path.join(output_path,folder_lists))
    #print (code_log)
        code_log = list(code_log)
        filename = str(scenario_no)+'_'+('_'.join(map(str,code_log)))
    #print (filename)
        file = open(output_path+folder_lists+'/'+filename+'.txt','w')
        file.write("code \t vp \t vs \t rho \t ephi \t vsh \t sw \n")
        for entry in zipped:
        #file.write("%f \n" % entry)
            file.write("%s \t %f \t %f \t %f \t %f \t %f \t %f \n" % entry)
        scenario_no = scenario_no + 1

    return all_models_list

def create_logs(database, layers, thickness, log_interval, start_depth):
    #n = len(database)
    n = 4
    database = database.T
    scenario_list = database[0]
    vp_list = database[1]
    vs_list = database[2]
    rho_list = database[3]
    ephi_list = database[4]
    vsh_list = database[5]
    sw_list = database[6]

    thickness = np.array(thickness)
    int_thickness = np.round((thickness/log_interval),decimals = 0)
    grid = list(product(range(n),repeat = layers))

    scenario_no = 1

    all_models = []

    for iteration in grid:
        #print (iteration)
        scenario_log = []
        depth_log = []
        vp_log = []
        vs_log = []
        rho_log = []
        ephi_log = []
        vsh_log = []
        sw_log = []
        filename_log = []

        l = len(iteration) # n = total number of layers
        #print (l)
        i = 0
        while i < l:
            position = iteration[i] # i = layer number, position = which facies in database
            if i == 0:
                layer_z_start = start_depth
                layer_z_stop = (start_depth + log_interval * int_thickness[i])
            else:
                layer_z_start = (start_depth + log_interval * i * int_thickness[i-1])
                layer_z_stop = (layer_z_start + log_interval * int_thickness[i])
            #print (layer_z_start, layer_z_stop, log_interval)

            scenario_log.append([scenario_list[position]]*int_thickness[i])
            filename_log.append([scenario_list[position]])
            depth = np.arange(layer_z_start, layer_z_stop, log_interval)
            #print (depth)
            depth_log.append(depth)
            vp_log.append([vp_list[position]]*int_thickness[i])
            vs_log.append([vs_list[position]]*int_thickness[i])
            rho_log.append([rho_list[position]]*int_thickness[i])
            ephi_log.append([ephi_list[position]]*int_thickness[i])
            vsh_log.append([vsh_list[position]]*int_thickness[i])
            sw_log.append([sw_list[position]]*int_thickness[i])
            i = i + 1
        depth_log = [float(j) for j in (np.hstack(depth_log))]
        vp_log = [float(j) for j in (np.hstack(vp_log))]
        vs_log = [float(j) for j in (np.hstack(vs_log))]
        rho_log = [float(j) for j in (np.hstack(rho_log))]
        ephi_log = [float(j) for j in (np.hstack(ephi_log))]
        vsh_log = [float(j) for j in (np.hstack(vsh_log))]
        sw_log = [float (j) for j in (np.hstack(sw_log))]
        scenario_log = list(np.hstack(scenario_log))
        filename_log = list(np.hstack(filename_log))
        #print(code_log)

        zipped = list(zip(scenario_log,depth_log,vp_log,vs_log, rho_log, ephi_log, vsh_log, sw_log))
        all_models.append(zipped)
        #print (all_models)
        #print (zipped)
        #print (vp_log)
        #print (type(vp_log))

        if not os.path.exists(os.path.join(output_path,folder)):
            os.makedirs(os.path.join(output_path,folder))
        #print (code_log)
        #code_log = list(code_log)
        filename = str(scenario_no)+'_'+('_'.join(map(str,filename_log)))
        #print (filename)
        file = open(output_path+folder+'/'+filename+'.txt','w')
        file.write("code \t depth \t vp \t vs \t rho \t ephi \t vsh \t sw \n")
        for entry in zipped:
            #file.write("%f \n" % entry)
            file.write("%s \t %f \t %f \t %f \t %f \t %f \t %f \t %f \n" % entry)
        scenario_no = scenario_no + 1

    return all_models



#output = create_logs(database, n, layers, thickness, log_interval, start_depth)
#output_lists = create_lists(database, n, layers)
#print (output_lists)
"""
#print (grid)
#print(len(grid))

#print (database)
#vp = database[2]
#n = vp[0]
#print (vp)
#print (n)


def create_logs(database, n, layers, thickness):
    i = 1
    while i <= n:
        facies = database[i]
        vp_1 = facies[3]
        vs_1 = facies[4]
        rho_1 = facies[5]

        j = 1
        while j <= n:
            facies = database[j]
"""




