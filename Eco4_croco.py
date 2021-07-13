'''
Created on Jan 29, 2019
Here we define Time in function so that it can be used in other modules (files)
We also define Eco, the main function for computing ecosystems based on N
@author: Keisuke
'''

from pylab import *

def Time():
    tMax = 4 #(d)
    dt= tMax/1000
    tMin = 0
    t = arange(tMin,tMax+dt,dt)
    return t,dt

def Eco(M,K,m,S,X0,a,b,c,d,e,f,g,h):
    
    t,dt = Time()
    U = arange(size(t))
    
    o = zeros(size(t))
    
    Ncro = copy(o)   #(cell L-1)
    Noth = copy(o)   #(cell L-1)
    NH4 = (a*t**3+b*t**2+c*t+d)/1000    #(umol L-1)
    NH4[NH4<0] = 0
    NO3 = (e*t**3+f*t**2+g*t+h)/1000    #(umol L-1)
    NO3[NO3<0] = 0
    
    
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
    
    Ncro[0] = X0[0]
    Noth[0] = X0[1]
    
    for i in U[:-1]:
        dNcroDt = (M1*NO3[i]/(NO3[i]+K1) + M2*NH4[i]/(NH4[i]+K2))*Ncro[i] - mcro*Ncro[i]
        dNothDt = (M3*NO3[i]/(NO3[i]+K3) + M4*NH4[i]/(NH4[i]+K4))*Noth[i] - moth*Noth[i]
        
        Ncro[i+1] = Ncro[i] + dNcroDt*dt
        Noth[i+1] = Noth[i] + dNothDt*dt
    
    return Ncro,Noth,NO3,NH4


