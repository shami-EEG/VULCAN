import numpy as np
import scipy

au = 1.4959787E13  # cm
r_sun = 6.957E10 # cm
ly = 63241.1*au
hc = 1.98644582E-9 # Planck constant times the light speed (erg nm)
pc = 3.086e+18 # pc to cm 

# Epsilon Eridani is 10.475 light years away and with 0.735 solar radius
# GJ876 is 15.2 light years away and has 0.3761 solar radius
# 51 Eridani is 95.9 light years away and with 1.45 solar radius

new_str = '# WL(nm)    Flux(ergs/cm**2/s/nm)\n'

eri_51 = np.genfromtxt('../atm/stellar_flux/51_eri_IUE.txt',names=['A','ergcmA'],skip_header=18)
grid_7K = np.genfromtxt('../../../../../Bern/python/Coding_test/vulcan_claire_loop/atm/stellar_flux/T7000K.txt',names=['ld','flux'])
#sun = np.genfromtxt('../atm/stellar_flux/Gueymard_solar.txt', names=['lambda','flux'], dtype=None, skip_header=1)
HR8799 = np.genfromtxt('../atm/stellar_flux/hr8799_simulspec.dat', names=['A','ph'], dtype=None, skip_header=1)

for _,lmd in enumerate(HR8799['A']):
    if lmd < 115.058 *10. and lmd > 10.:
        new_str += '{:<8.3f}'.format(lmd*0.1) + "{:>12.6E}".format(HR8799['ph'][_]*10.* (hc/(lmd*0.1)) *(39.94*pc/(r_sun*1.34))**2 ) + '\n'


for _,lmd in enumerate(eri_51['A']):
    new_str += '{:<8.3f}'.format(lmd*0.1) + "{:>12.6E}".format(eri_51['ergcmA'][_]*10.  *(95.9*ly/(r_sun*1.45))**2) + '\n'
    
for _,ld in enumerate(grid_7K['ld']):
    if ld>197.8 and ld<=800.:
        new_str += '{:<8.3f}'.format(ld) + "{:>12.6E}".format(grid_7K['flux'][_] *4.996) + '\n'
    
    
    
    
    
# with open('../atm/stellar_flux/51_eri_IUE.txt') as f: # wl was in Angstroms in the file
#     for line in f.readlines():
#         if not line.startswith("#") and line.split():
#             li = line.split()
#             #wl = float(li[0])*0.1
#             #flux = float(li[1])*10. *(10.475*63241*au/r_sun*0.735)**2     # eps Eradian is 10.475 light years away
#             wl = float(li[0])
#             flux = float(li[1])
#             if flux > 0:
#                 new_str += '{:<8.3f}'.format(float(wl)) + "{:>12.2E}".format(flux) + '\n'

# with open('../atm/stellar_flux/Gueymard_solar.txt') as f:
#     for line in f.readlines():
#         if not line.startswith("#") and line.split():
#             li = line.split()
#             if float(li[0]) >= 283.:
#                 new_str += '{:<8.3f}'.format(float(li[0])) + "{:>12.2E}".format(float(li[1]) *0.1) + '\n'
#             else: pass

    
#with open('sflux-HD189_Moses11.txt', 'w+') as f: f.write(new_str)   
with open('../atm/stellar_flux/sflux-51-Eri-IUE.txt', 'w+') as f: f.write(new_str)  