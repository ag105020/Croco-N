'''
Created on 07/12/2020
Using new data and focusing only on Pro and Syn
@author: Keisuke
From p000 02 03
'''

from pylab import *
from FigSetting2 import *
from Eco4_croco import *
from Tools23 import *
#from Tools21 import * #Same range
from Savefig3 import *

rcParams.update({'font.size': 12})

rcParams.update({'lines.linewidth':2})

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

#=== Initial N concentrations (umol L-1) =========
#---NH4 adding case--------
N0no3nh4 = 0.003
N0nh4nh4 = 0.10

#---NO3 adding case--------
N0no3no3 = 0.1
N0nh4no3 = 0.015

#---Control case-----------
N0no3cont= 0.003
N0nh4cont= 0.015

################################################
# Main calculation
################################################
#=====NH4 adding case ========
a=-4;b=34.5;c=-98.5;d=99;e=1;f=-3.5;g=3.5;h=3 
S,X0,N0 = Convert(S,X0,N0,Sno3nh4,Snh4nh4,X0croNH4,X0othNH4,N0no3nh4,N0nh4nh4)
Xcro,Xoth,NO3,NH4 = Eco(M,K,m,S,X0,a,b,c,d,e,f,g,h)

figure(1,figsize=(7,5.5)) 

fig(1,0,6,Xcro,Xoth,NO3,NH4)
#--Legend--
subplot(2,2,3)
errorbar([],[],[],fmt='o',color='#800000',markeredgecolor='k',elinewidth=1,ecolor='k',capthick=1,capsize=8,zorder=11,label='Data')
plot([],[],label='Model',color='#800000')
legend(loc=2,edgecolor='k',fontsize=12)

subplot(2,2,4)
errorbar([],[],[],fmt='o',color='#FF9900',markeredgecolor='k',elinewidth=1,ecolor='k',capthick=1,capsize=8,zorder=11,label='Data')
plot([],[],label='Model',color='#FF9900')
legend(loc=2,edgecolor='k',fontsize=12)
 
# subplot(3,5,4)
# errorbar([],[],[],fmt='o',color='#FF7F0E',markeredgecolor='k',elinewidth=1,ecolor='k',capthick=1,capsize=8,zorder=11,label='Data')
# plot([],[],label='Model',color='#1D75B3')
# #legend(loc=1,edgecolor='k')
#  
#NO3 adding case ========
a=-1.6667;b=11;c=-21.333;d=15;e=14.667;f=-67.5;g=47.833;h=96
S,X0,N0 = Convert(S,X0,N0,Sno3no3,Snh4no3,X0croNO3,X0othNO3,N0no3no3,N0nh4no3)
Xcro,Xoth,NO3,NH4 = Eco(M1,K1,m,S,X0,a,b,c,d,e,f,g,h)
fig(1,2,10,Xcro,Xoth,NO3,NH4)
 
gcf().tight_layout()
#=====Control case ===========
# a=-5.3333;b=25.5;c=-32.167;d=15;e=0.8333;f=-2.5;g=1.6667;h=3
# S,X0,N0 = Convert(S,X0,N0,Sno3cont,Snh4cont,X0croCont,X0othCont,N0no3cont,N0nh4cont)
# Xcro,Xoth,NO3,NH4 = Eco(M,K,m,S,X0,a,b,c,d,e,f,g,h)
# fig(1,10,2,Xcro,Xoth,NO3,NH4)
 
Savefig3('02\\13 Croco N','Cell N',300)

show() 


