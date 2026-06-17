import sys
sys.path.insert(0, '../') # including the upper level of directory for the path of modules

import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.legend as lg
import vulcan_cfg
try: from PIL import Image
except ImportError: 
    try: import Image
    except: vulcan_cfg.use_PIL = False
import os, sys
import pickle


vul_data = '../output/'
vul_data2 = '../output/'


# Setting the 2rd input argument as the species names to be plotted (separated by ,)
plot_spec = sys.argv[1]
# Setting the 3th input argument as the output eps filename        
plot_name = sys.argv[2]

plot_dir = '../'+ vulcan_cfg.plot_dir

# taking user input species and splitting into separate strings and then converting the list to a tuple
plot_spec = tuple(plot_spec.split(','))
nspec = len(plot_spec)

# These are the "Tableau 20" colors as RGB.    
tableau20 = [(31, 119, 180),(255, 127, 14),(44, 160, 44),(214, 39, 40),(148, 103, 189),(140, 86, 75), (227, 119, 194),(127, 127, 127),(188, 189, 34),(23, 190, 207),\
(174, 199, 232),(255, 187, 120),(152, 223, 138),(255, 152, 150),(197, 176, 213),(196, 156, 148),(247, 182, 210),(199, 199, 199),(219, 219, 141),(158, 218, 229)] 

# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.    
for i in range(len(tableau20)):    
    r, g, b = tableau20[i]    
    tableau20[i] = (r / 255., g / 255., b / 255.)
    
tex_labels = {'H':'H','H2':'H$_2$','O':'O','OH':'OH','H2O':'H$_2$O','CH':'CH','C':'C','CH2':'CH$_2$','CH3':'CH$_3$','CH4':'CH$_4$','HCO':'HCO','H2CO':'H$_2$CO', 'C4H2':'C$_4$H$_2$',\
'C2':'C$_2$','C2H2':'C$_2$H$_2$','C2H3':'C$_2$H$_3$','C2H':'C$_2$H','CO':'CO','CO2':'CO$_2$','He':'He','O2':'O$_2$','CH3OH':'CH$_3$OH','C2H4':'C$_2$H$_4$','C2H5':'C$_2$H$_5$','C2H6':'C$_2$H$_6$','CH3O': 'CH$_3$O'\
,'CH2OH':'CH$_2$OH', 'CH3SCH3':'DMS', 'CH3S2CH3':"DMDS",'C6H6':'C$_6$H$_6$','H2S':'H$_2$S' ,'SO2':'SO$_2$' ,'CH3S':'CH$_3$S','CH3SH':'CH$_3$SH', 'CS2':'CS$_2$' ,'NH3':'NH$_3$', 'COS':"OCS"}


with open(vul_data, 'rb') as handle:
  data = pickle.load(handle)

try:
    with open(vul_data2, 'rb') as handle:
        data2 = pickle.load(handle)
    vulcan_spec2 = data2['variable']['species']
except: pass
try:
    with open(vul_data3, 'rb') as handle:
        data3 = pickle.load(handle)
    vulcan_spec3 = data3['variable']['species']
except: pass
        
    
color_index = 0
vulcan_spec = data['variable']['species']

#cea = np.genfromtxt('../cea_chem_iso1400K.txt', names=True ) # taking the first column 

# for i in range(1, data['variable']['nr']):
#     ratio = data2['variable']['k'][i] / data['variable']['k'][i]
#     if np.amax(ratio) > 2. or np.amin(ratio) < 0.5:
#         print (i)
#         print (ratio)


for color_index,sp in enumerate(plot_spec):
    if color_index == len(tableau20): # when running out of colors
        tableau20.append(tuple(np.random.rand(3)))
    if sp in tex_labels: sp_lab = tex_labels[sp]
    else: sp_lab = sp
    if sp in data['variable']['species']:
        plt.plot(data['variable']['ymix'][:,vulcan_spec.index(sp)], data['atm']['pco']/1.e6, color=tableau20[color_index], label=sp_lab, alpha=0.9)
        plt.plot(data['variable']['y_ini'][:,vulcan_spec.index(sp)]/data['atm']['n_0'], data['atm']['pco']/1.e6, color=tableau20[color_index], ls=':',lw=1.2, alpha=0.9)
    
    # try: plt.plot(cea[sp], cea['P'], color=tableau20[color_index], ls='--',  alpha=0.9)
    # except: pass
    #
    # if sp=='S':
    #     plt.scatter(2.5238E-10, 1. , color=tableau20[color_index])
    # elif sp=='S2':
    #     plt.scatter(4.5788E-10, 1. , color=tableau20[color_index])
    # elif sp=='SH':
    #     plt.scatter(2.2775E-07, 1. , color=tableau20[color_index])
    # elif sp=='SO':
    #     plt.scatter(9.4945E-12, 1. , color=tableau20[color_index])
    # elif sp=='H2S':
    #     plt.scatter(1.3117E-04, 1. , color=tableau20[color_index])
    #       
    
    try:
        if sp in data2['variable']['species']:
            plt.plot(data2['variable']['ymix'][:,vulcan_spec2.index(sp)], data2['atm']['pco']/1.e6, color=tableau20[color_index], ls='--',lw=1.5, alpha=0.9)
            #plt.plot(data2['variable']['y_ini'][:,vulcan_spec2.index(sp)]/data2['atm']['n_0'], data2['atm']['pco']/1.e6, color=colors[color_index], ls=':',lw=1.2, alpha=0.9)
    except: pass
    try:
        if sp in data3['variable']['species']:
            plt.plot(data3['variable']['ymix'][:,vulcan_spec3.index(sp)], data3['atm']['pco']/1.e6, color=tableau20[color_index], ls='-.',lw=1.5, alpha=0.9)
    except: pass        
    # if sp in data4['variable']['species']:
    #     plt.plot(data4['variable']['ymix'][:,vulcan_spec4.index(sp)], data4['atm']['pco']/1.e6, color=tableau20[color_index], ls='-.',lw=1.2, alpha=0.9, label='')


plt.gca().set_xscale('log')
plt.gca().set_yscale('log')
plt.gca().invert_yaxis()
plt.xlim((1.E-12, 0.9))
plt.ylim((data['atm']['pco'][0]/1.e6, data['atm']['pco'][-1]/1.e6))
plt.legend(frameon=0, prop={'size':12}, loc=3)
plt.xlabel("Mixing Ratio",fontsize=12)
plt.ylabel("Pressure (bar)",fontsize=12)
#plt.ylabel("Height (km)")
#plt.title('HD209b')
plt.savefig(plot_dir + plot_name + '.png')
# plt.savefig(plot_dir + plot_name + '.eps')
if vulcan_cfg.use_PIL == True:
    plot = Image.open(plot_dir + plot_name + '.png')
    plot.show()
else: plt.show()

