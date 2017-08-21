__author__ = 'wallisj'

import matplotlib.pyplot as plt
import matplotlib.colors as clr
import numpy as np
import matplotlib.cm as cm
#import matplotlib.cm as cmaps
from A3_define_parameters import filepath, header_lines, output_path, folder, folder_lists, folder_interfaces, n, layers, thickness, log_interval, start_depth

from A1_load_database import data_load
from A2_define_model import create_logs, create_lists, all_interfaces
from C2_Calculate_Moduli import calc_moduli
from C3_shuey import shuey_two

database = data_load(filepath, header_lines)

# half space modelling
def half_space(database):

    blocky_list = np.array(all_interfaces(database))
#print (blocky_list[0])
    code1 = []
    code2 = []
    vp1 = []
    vp2 = []
    vs1 = []
    vs2 = []
    rho1 = []
    rho2 = []
    ephi1 = []
    ephi2 = []
    vsh1 = []
    vsh2 = []
    sw1 = []
    sw2 = []
    r0_list = []
    g_list = []

    model1 = blocky_list[1]
    print (model1)

    for model in blocky_list:
        model = model.T
        code = model[0]
        vp = [float(j) for j in (model[1])]
        vs = [float(j) for j in (model[2])]
        rho = [float(j) for j in (model[3])]
        ephi = [float(j) for j in (model[4])]
        vsh = [float(j) for j in (model[5])]
        sw = [float(j) for j in (model[6])]

        i = 0
        while i < 1:
            #interface_no = i+1
            #print (vp[i])
            #print (vp[i+1])
            avo = shuey_two(vp[i], vp[i+1], vs[i], vs[i+1], rho[i], rho[i+1])
            r0 = avo[0]
            g = avo[1]
            code1.append(code[i])
            code2.append(code[i+1])
            vp1.append(vp[i])
            vp2.append(vp[i+1])
            vs1.append(vs[i])
            vs2.append(vs[i+1])
            rho1.append(rho[i])
            rho2.append(rho[i+1])
            ephi1.append(ephi[i])
            ephi2.append(ephi[i+1])
            vsh1.append(vsh[i])
            vsh2.append(vsh[i+1])
            sw1.append(sw[i])
            sw2.append(sw[i+1])
            r0_list.append(r0)
            g_list.append(g)

            i = i + 1
        #print (vsh1)
    return (vp1, vp2, vs1, vs2, rho1, rho2, ephi1, ephi2, vsh1, vsh2, sw1, sw2, r0_list, g_list, code1, code2)

# map facies to facies number

def map_facies(database):
    database = database.T
    code_list = database[0]
    n = len(code_list)
    facies_map = range(1,n+1, 1)
    facies_dictionary = dict(zip(facies_map, code_list))

    return facies_dictionary
    #for a, b in facies_dictionary.items():
        #print (a,b)

#x = map_facies(database)



#half_model = half_space(database, n, layers)

def plot_half_space(database):
    half_model = half_space(database)
    vp1 = half_model[0]
    vp2 = half_model[1]
    vs1 = half_model[2]
    vs2 = half_model[3]
    rho1 = half_model[4]
    rho2 = half_model[5]
    ephi1 = half_model[6]
    ephi2 = half_model[7]
    vsh1 = half_model[8]
    vsh2 = half_model[9]
    sw1 = half_model[10]
    sw2 = half_model[11]
    intercept = half_model[12]
    gradient = half_model[13]
    code1 = half_model[14]
    code2 = half_model[15]

    facies_dictionary = map_facies(database)
    n = len(database)
    #print (n)
    area = np.pi*2**2
    cmap = plt.cm.get_cmap('nipy_spectral')

    #print(cmap.N)
    #extract all colours from the colour map http://stackoverflow.com/questions/14777066/matplotlib-discrete-colorbar
    cmaplist = [cmap(i) for i in range(cmap.N)]
    facies_cmap = cmap.from_list('custom_jw', cmaplist,cmap.N)
    #print (cmap.N)

    #define the bins and normalise
    bounds = np.linspace(1,n,n)
    #cmap.N = no.colours? property of the colourbar --> bin into bounds

    facies_norm = clr.BoundaryNorm(bounds,cmap.N)

    facies_no_upper = []
    facies_no_lower = []
    #print (code1)
    for upper in code1:
            for facies_no, code in facies_dictionary.items():
                if code == upper:
                    facies_no_upper.append(facies_no)

    for lower in code2:
        for facies_no, code in facies_dictionary.items():
            if code == lower:
                facies_no_lower.append(facies_no)

    #print (facies_dictionary)
    #print (len(code1))
    #print(len(facies_no_upper))
    #print(len(intercept))

    #print(facies_no_lower)
    #facies_no_upper = [float(j) for j in facies_no_upper]
    #print (type(facies_no_upper))
    #print (type(intercept))
    #print (intercept)
    labels = list(facies_dictionary.values())
    #print (labels)
    #print (type(labels))
    print (ephi1)

    sw_cmap = plt.cm.get_cmap('jet_r')
    sw_norm = plt.Normalize(vmin = 0, vmax = 1)

    #plt.register_cmap(name = 'viridis',cmap=viridis)
    ephimax = max(max(ephi1),max(ephi2))
    ephi_cmap =plt.cm.get_cmap('gnuplot')
    ephi_norm = plt.Normalize(vmin = 0, vmax = ephimax)

    vsh_cmap =plt.cm.get_cmap('afmhot_r')
    vsh_norm = plt.Normalize(vmin = 0, vmax = 1)

    fig, ((ax1, ax2, ax3, ax4),(ax5, ax6, ax7, ax8)) = plt.subplots(2,4)
    fig.suptitle('Half Space Models: I-G for all possible interfaces in database')

    upperfac = ax1.scatter(intercept, gradient, c = facies_no_upper, cmap = facies_cmap, s=area, edgecolors = 'none', norm = facies_norm)
    ax1.set_xlabel('Intercept')
    ax1.set_ylabel('Gradient')
    ax1.axhline()
    ax1.axvline()
    #ax1.axhline(y=0, xmin = 0, xmax = 1, color = 'black')
    #ax1.axvline(x=0, ymin = 0, ymax = 1, color = 'black')

    cb1 = plt.colorbar(upperfac, ax=ax1)
    #print (bounds)
    loc = bounds + 0.5
    #print(loc)
    cb1.set_ticks(loc)
    cb1.set_ticklabels(labels)
    cb1.ax.tick_params(labelsize=8)
    cb1.set_label('Upper Facies')

    upperfluid = ax2.scatter(intercept, gradient, c = sw1, cmap = sw_cmap, s=area, edgecolors = 'none', norm = sw_norm)
    ax2.set_xlabel('Intercept')
    ax2.set_ylabel('Gradient')
    ax2.axhline()
    ax2.axvline()

    cb2 = plt.colorbar(upperfluid, ax=ax2)
    cb2.set_label('Upper Fluid Saturation (Sw)')

    upperphi = ax3.scatter(intercept, gradient, c = ephi1, cmap = ephi_cmap, s=area, edgecolors = 'none', norm = ephi_norm)
    ax3.set_xlabel('Intercept')
    ax3.set_ylabel('Gradient')
    ax3.axhline()
    ax3.axvline()

    cb3 = plt.colorbar(upperphi, ax=ax3)
    cb3.set_label('Upper Eff. Porosity')

    uppervsh = ax4.scatter(intercept, gradient, c = vsh1, cmap = vsh_cmap, s=area, edgecolors = 'none', norm = vsh_norm)
    ax4.set_xlabel('Intercept')
    ax4.set_ylabel('Gradient')
    ax4.axhline()
    ax4.axvline()

    cb4 = plt.colorbar(uppervsh, ax=ax4)
    cb4.set_label('Upper VShale')



    lowerfac = ax5.scatter(intercept, gradient, c = facies_no_lower, cmap = facies_cmap, s=area, edgecolors = 'none', norm = facies_norm)

    cb5 = plt.colorbar(lowerfac, ax=ax5)
    #print (bounds)
    loc = bounds + 0.5
    #print(loc)
    cb5.set_ticks(loc)
    cb5.set_ticklabels(labels)
    cb5.ax.tick_params(labelsize=8)
    cb5.set_label('Lower Facies')

    ax5.set_xlabel('Intercept')
    ax5.set_ylabel('Gradient')
    ax5.axhline()
    ax5.axvline()

    lowerfluid = ax6.scatter(intercept, gradient, c = sw2, cmap = sw_cmap, s=area, edgecolors = 'none', norm = sw_norm)
    ax6.set_xlabel('Intercept')
    ax6.set_ylabel('Gradient')
    ax6.axhline()
    ax6.axvline()

    cb6 = plt.colorbar(lowerfluid, ax=ax6)
    cb6.set_label('Lower Fluid Saturation (Sw)')

    lowerphi = ax7.scatter(intercept, gradient, c = ephi2, cmap = ephi_cmap, s=area, edgecolors = 'none', norm = ephi_norm)
    ax7.set_xlabel('Intercept')
    ax7.set_ylabel('Gradient')
    ax7.axhline()
    ax7.axvline()

    cb7 = plt.colorbar(lowerphi, ax=ax7)
    cb7.set_label('Lower Eff. Porosity')

    lowervsh = ax8.scatter(intercept, gradient, c = vsh2, cmap = vsh_cmap, s=area, edgecolors = 'none', norm = vsh_norm)
    ax8.set_xlabel('Intercept')
    ax8.set_ylabel('Gradient')
    ax8.axhline()
    ax8.axvline()

    cb8 = plt.colorbar(lowervsh, ax=ax8)
    cb8.set_label('Lower VShale')

    #fig.tight_layout()
    plt.subplots_adjust(left=0.02, right=0.98, top=0.95, bottom=0.05)

    plt.show(fig)

plot_half_space(database)

