'''
Created on Feb 1, 2019

@author: Keisuke
'''

from pylab import *
from Eco0 import Time

Xlabel = 'time (d)'
tData = [nan,nan,0,1,2,3]
Cell3 = genfromtxt('..//Data//CellCountAveCro.csv',delimiter=',').T
CellSD = genfromtxt('..//Data//CellCountSD_Cro.csv',delimiter=',').T
Nut3 = genfromtxt('..//Data//NutAve3.csv',delimiter=',').T
NutSD = genfromtxt('..//Data//NutSD3.csv',delimiter=',').T
t,dt = Time()

def SubPl(loc,Title,y,Ylabel,Color):
    subplot(2,2,loc)
    plot(t,y,Color,zorder=10)
    xlabel(Xlabel)
    ylabel(Ylabel)
    xlim(right=3.3)
    xticks(arange(4))
    ylim(bottom=0)
    title(Title,y=1.02)

def fig(FigNum,SubPlNum,Ex,Xcro,Xoth,NO3,NH4):
#    figure(FigNum,figsize=(8,6)) 
    #For Pro#
    SubPl(SubPlNum + 1,'Croco',Xcro*1000,'Cell N (nmol L$^{-1}$)',Color = '#800000')
    errorbar(tData,Cell3[Ex],CellSD[Ex],fmt='o',color='#800000',markeredgecolor='k',elinewidth=1,ecolor='k',capthick=1,capsize=8,zorder=11)
    ylim(0,40)
#     if SubPlNum == 5:
#         ylim(0,30)
#     elif SubPlNum == 10:
#         ylim(0,30)
#    ylim(0,60000)
    #For Syn#
    SubPl(SubPlNum + 2,'Other',Xoth*1000,'Cell N (nmol L$^{-1}$)',Color = '#FF9900')
    errorbar(tData,Cell3[Ex+1],CellSD[Ex+1],fmt='o',color='#FF9900',markeredgecolor='k',elinewidth=1,ecolor='k',capthick=1,capsize=8,zorder=11)
    ylim(0,40)
# #     if SubPlNum == 5:
# #         ylim(0,15)
# #     elif SubPlNum == 10:
# #         ylim(0,15)
# #    ylim(0,6000)
#     #For NH4#
#     SubPl(SubPlNum + 5,'NH$_4^+$',NH4*1e3,'NH$_{4}^{+}$ (nmol L$^{-1}$)')
#     errorbar(tData,Nut3[Ex],NutSD[Ex],fmt='o',color='#FF7F0E',markeredgecolor='k',elinewidth=1,ecolor='k',capthick=1,capsize=8,zorder=11)
#     ylim(0,150)
# #     if SubPlNum == 5:
# #         ylim(0,20)
# #     elif SubPlNum == 10:
# #         ylim(0,20)
#     
#     #For NO3#
#     SubPl(SubPlNum + 4,'NO$_3^-$',NO3*1e3,'NO$_{3}^{-}$ (nmol L$^{-1}$)')
#     errorbar(tData,Nut3[Ex+1],NutSD[Ex+1],fmt='o',color='#FF7F0E',markeredgecolor='k',elinewidth=1,ecolor='k',capthick=1,capsize=8,zorder=11)
#     ylim(0,150)
# #     if SubPlNum == 0:
# #         ylim(0,15)
# #     elif SubPlNum == 10:
# #         ylim(0,15)
    
def Convert(S,X0,N0,Sno3,Snh4,X0cro,X0oth,N0no3,N0nh4):
    S[0] = Sno3
    S[1] = Snh4
    X0[0] = X0cro
    X0[1] = X0oth
    N0[0] = N0no3
    N0[1] = N0nh4
    return S,X0,N0