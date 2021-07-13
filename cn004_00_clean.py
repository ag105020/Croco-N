'''
Created on 07/12/2020
Using new data and focusing only on Pro and Syn
@author: Keisuke
From p000 02 03
'''

from pylab import *
from FigSetting2 import *
from Eco4_croco import *
from Tools22 import *
#from Tools21 import * #Same range
from Savefig3 import *

#rcParams.update({'font.size': 15})
    
#======Preparing arrays=======
M = zeros(7); K = copy(M); m = zeros(3); S = zeros(2); X0 = zeros(2); N0 = zeros(3)
M1 = zeros(7); K1 = copy(M)
########################################################################################
# Parameterization
########################################################################################
conv = 1/1000 #(umol/nmol) Unit conversation factor
#======Defining values common for all the cases=====
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#oooooooooooooooooooooooooooooooooooooooo
# NH4+ added
#oooooooooooooooooooooooooooooooooooooooo
#----- Mu max (d-1)--------------------
M[1] = 2.8 #(d-1) MuMaxCroNO3    3
M[2] = 6.6 #(d-1) MuMaxCroNH4    7
M[3] = 1.8 #(d-1) MuMaxOthNO3    1
M[4] = 1.1  #(d-1) MuMaxOthNH4   1.3

#----- Ks (umol L-1)-------------------
K[1] = 0.08 #(umol L-1) KsCroNO3    0.1
K[2] = 0.14 #(umol L-1) KsCroNH4    0.07
K[3] = 0.5 #(umol L-1) KsOthNO3    0.05
K[4] = 0.006 #(umol L-1) KsOthNH4    0.01

#=== Initial cell N concentration in the environment (umol / L) ===========
#-----NH4 adding case---------
X0croNH4 = 2.5*conv     #2.4
X0othNH4 = 5.0*conv       #5

#----- mortality (d-1)-----------------
m[0] = 0.4 #(d-1) mCro    1.0
m[1] = 0.4 #(d-1) mOth    0.5
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

#oooooooooooooooooooooooooooooooooooooooo
# NO3- added
#oooooooooooooooooooooooooooooooooooooooo
#----- Mu max (d-1)--------------------
M1[1] = 1.3 #(d-1) MuMaxCroNO3
M1[2] = 8 #(d-1) MuMaxCroNH4
M1[3] = 0.5 #(d-1) MuMaxOthNO3
M1[4] = 0.9  #(d-1) MuMaxOthNH4

#----- Ks (umol L-1)-------------------
K1[1] = 0.09 #(umol L-1) KsCroNO3
K1[2] = 0.07 #(umol L-1) KsCroNH4
K1[3] = 0.7 #(umol L-1) KsOthNO3
K1[4] = 0.002 #(umol L-1) KsOthNH4

#=== Initial cell N concentration in the environment (umol / L) ===========
X0croNO3 = 4.36*conv
X0othNO3 = 5.83*conv

#=== Source term of XXX under XXX addition (or control) (umol L-1 d-1) ==========
#---NH4 adding case------
Sno3nh4 = 0.01
Snh4nh4 = -0.03

#---NO3 adding case------
Sno3no3 = -0.000
Snh4no3 = -0.000

#---Control case---------
Sno3cont= -0.000
Snh4cont= -0.000

#-----Control case------------
X0croCont= 4.36*conv
X0othCont= 6.83*conv

################################################
# Main calculation
################################################

tMax = 10 #(d)
dt= tMax/10000
tMin = 0
t = arange(tMin,tMax+dt,dt)
    
U = arange(size(t))
 
o = zeros(size(t))

#########Nutrient#############
NH4 = 0.001
NO3 = 0.001
##############################

Ncro = copy(o)   #(cell L-1)
Noth = copy(o)   #(cell L-1)
Nzoo = copy(o)
MuCro = copy(o)
NH4 = NH4*ones(size(t))
NO3 = NO3*ones(size(t))

M1 = M[1] #(d-1) MuMaxNO3 Croco
M2 = M[2] #(d-1) MuMaxNH4 Croco
M3 = M[3] #(d-1) MuMaxNO3 Other
M4 = M[4] #(d-1) MuMaxNH4 Other
 
K1 = K[1] #(umol L-1) KsNO3 Croco
K2 = K[2] #(umol L-1) KsNH4 Croco
K3 = K[3] #(umol L-1) KsNO3 Other
K4 = K[4] #(umol L-1) KsNH4 Other
 
mcro = m[0] #(d-1)
moth = m[1] #(d-1)
 
Ncro[0] = 1
Noth[0] = 1
Nzoo[0] = 1

Gmax = 7.5
Kg = 5
m2 = 0.01

fN2 = 0.3 #N2 fixation fraction for total
Nfix = 1/(1-fN2)*fN2
Nfix = 0
#Nfix = 0

for i in U[:-1]:
    Gcro = Gmax*(Ncro[i]**2/(Ncro[i]**2+Noth[i]**2))*((Ncro[i]+Noth[i])**2/(Kg**2+(Ncro[i]+Noth[i])**2))
    Goth = Gmax*(Noth[i]**2/(Ncro[i]**2+Noth[i]**2))*((Ncro[i]+Noth[i])**2/(Kg**2+(Ncro[i]+Noth[i])**2))
    
    dNcroDt = (M1*NO3[i]/(NO3[i]+K1) + M2*NH4[i]/(NH4[i]+K2))*Ncro[i]*(1+Nfix) - Nzoo[i]*Gcro#- mcro*Ncro[i]
    dNothDt = (M3*NO3[i]/(NO3[i]+K3) + M4*NH4[i]/(NH4[i]+K4))*Noth[i] - Nzoo[i]*Goth #- moth*Noth[i]
    dZoo = Nzoo[i]*(Gcro + Goth) - m2*Nzoo[i]**2
    
    Ncro[i+1] = Ncro[i] + dNcroDt*dt
    Noth[i+1] = Noth[i] + dNothDt*dt
    Nzoo[i+1] = Nzoo[i] + dZoo*dt
    
    MuCro[i] = (M1*NO3[i]/(NO3[i]+K1) + M2*NH4[i]/(NH4[i]+K2))*(1+Nfix)
    
#=====NH4 adding case ========
Colors = ['#800000','#FF9900']
figure(2,figsize=(6,5))
plot(t,Ncro*1e3,label='Croco',color=Colors[0])
plot(t,Noth*1e3,label='Other',color=Colors[1])
yscale('log')
ylabel('Cell N (nmol L$^{-1}$)')
xlabel('t (d)')
xlim(0,10)
ylim(1e1,1e4)
legend(edgecolor='k')

Savefig3('02\\13 Croco N','NH4_no_N2_0.001',300)

figure(1,figsize=(6,5))
plot(t,MuCro)

show() 


