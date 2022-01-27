#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 10:54:04 2021

@author: patrykkwoczak
"""
import numpy as np
import matplotlib.pyplot as plt
import imageio
import os
import time

start_time = time.time()

def hMap(a,b,x,y):
    return 1 - a*x**2 + b*y
    


def backwards_hMap(a,b,x,y):
    return -(1/b)*(1 - a*y**2 - x)

def hMap_n(a,b,x,y,n):
    x_i = x
    y_i = y
    
    for i in range(n):
        old_x = x_i
        old_y = y_i
        
        new_x = hMap(a,b,old_x,old_y)
        new_y = old_x
        
        x_i = new_x
        y_i = new_y
        
        if not(np.isfinite(x_i)):
            break
        if np.abs(x_i) > 100 or np.abs(y_i) > 100 :
            
            break
        
    x_n, y_n = x_i,y_i
    return [x_n, y_n]

dens_tan=1051
ba_list = np.loadtxt("new_per6Tan_ba_bac.txt").reshape(dens_tan, 2)
b_listB,a_listB = np.zeros(dens_tan),np.zeros(dens_tan)
for i in range(dens_tan):
    b_listB[i] = ba_list[i][0]
    a_listB[i] = ba_list[i][1]


# insert a,b,x,y of 2nd tangency line
dens_tan=1753
ba_list = np.loadtxt("new_per6Tan_ba_for.txt").reshape(dens_tan, 2)
b_listF,a_listF = np.zeros(dens_tan),np.zeros(dens_tan)
for i in range(dens_tan):
    b_listF[i] = ba_list[i][0]
    a_listF[i] = ba_list[i][1]


b_list_per6 = np.concatenate([np.flip(b_listB),b_listF])
a_list_per6 = np.concatenate([np.flip(a_listB),a_listF])

b_vals, a_vals =b_list_per6, a_list_per6

b_vals = [-0.30289999999999273, -0.30289387755101316, -0.30288775510203353, -0.30288163265305396, -0.3028755102040744, -0.30286938775509475, -0.3028632653061152, -0.3028571428571356, -0.302851020408156, -0.3028448979591764, -0.30283877551019683, -0.3028326530612172, -0.30282653061223763, -0.302820408163258, -0.30281428571427843, -0.30280816326529886, -0.30280204081631923, -0.30279591836733966, -0.3027897959183601, -0.30278367346938045, -0.3027775510204009, -0.3027714285714213, -0.3027653061224417, -0.3027591836734621, -0.30275306122448253, -0.3027469387755029, -0.30274081632652333, -0.30273469387754376, -0.30272857142856413, -0.30272244897958456, -0.302716326530605, -0.30271020408162536, -0.3027040816326458, -0.3026979591836662, -0.3026918367346866, -0.302685714285707, -0.30267959183672744, -0.3026734693877478, -0.30266734693876823, -0.3026612244897886, -0.30265510204080903, -0.30264897959182946, -0.30264285714284983, -0.30263673469387026, -0.3026306122448907, -0.30262448979591106, -0.3026183673469315, -0.3026122448979519, -0.3026061224489723, -0.3025999999999927]
a_vals = [1.3026819904544373, 1.3026963043723396, 1.3027106182763108, 1.3027249314737568, 1.3027392460417297, 1.3027535599040159, 1.3027678737497321, 1.3027821875856025, 1.3027965008094973, 1.3028108152113418, 1.3028251290031292, 1.3028394420514695, 1.3028537565447373, 1.3028680702944984, 1.3028823831022873, 1.3028966968444298, 1.3029110114596913, 1.3029253251533879, 1.3029396388310757, 1.302953952498211, 1.3029682661504256, 1.302982579788083, 1.3029968934117246, 1.3030112056195777, 1.3030255206169463, 1.3030398341985674, 1.3030541461336989, 1.3030684598673121, 1.3030827748592546, 1.3030970883822484, 1.3031114005559699, 1.303125715396644, 1.303140027674053, 1.3031543423468748, 1.3031686558023976, 1.303182969242521, 1.3031972818936977, 1.3032115960831694, 1.3032259094842575, 1.3032402228697226, 1.3032545362411283, 1.3032688491426292, 1.30328316271344, 1.3032974762713618, 1.3033117895103856, 1.3033261028881316, 1.3033404161756472, 1.3033547294502068, 1.3033690427082933, 1.30338335595347]

#b_list_per6[-10], a_list_per6[-10]
b_tan,a_tan = -0.212448, 1.51271  #sink6: -0.30266666666665937 , 1.3032274998595497


#dens_tan=1051
#ba_list = np.loadtxt("new_per6Tan_ba_bac.txt").reshape(dens_tan, 2)
#b_listB,a_listB = np.zeros(dens_tan),np.zeros(dens_tan)
#for i in range(dens_tan):
#    b_listB[i] = ba_list[i][0]
#    a_listB[i] = ba_list[i][1]
#
#
## insert a,b,x,y of 2nd tangency line
#dens_tan=1753
#ba_list = np.loadtxt("new_per6Tan_ba_for.txt").reshape(dens_tan, 2)
#b_listF,a_listF = np.zeros(dens_tan),np.zeros(dens_tan)
#for i in range(dens_tan):
#    b_listF[i] = ba_list[i][0]
#    a_listF[i] = ba_list[i][1]
#
#
#b_list_per6 = np.concatenate([b_listB,b_listF])
#a_list_per6 = np.concatenate([a_listB,a_listF])
#
#b_extra = np.flip(b_list_per6[0:14])
#a_extra = np.flip(a_list_per6[0:14])
#
#
#
#b = b_tan
#a_i = a_tan
#
#
#b_vals = np.concatenate([[b_tan],b_extra])
#a_vals = np.concatenate([[a_tan],a_extra])
dens=60000






x_conv,y_conv = np.zeros(dens),np.zeros(dens)
counter = 0
filenames = []

#a_vals = [a_tan]
a_i = a_tan
b,a_i =-0.435323, 2.25923 #-0.2124648095, 1.512665#3-coex: -0.212448, 1.51271

k = 0
counter = 0

#x_vals1 = np.linspace(0.8,0.85,dens)
#y_vals1 = np.linspace(-0.02,-0.02,dens)
#x_vals2 = np.linspace(1.125,1.2125,dens)
#y_vals2 = np.linspace(-0.02,-0.02,dens)
# np.concatenate([x_vals1,x_vals2]) np.concatenate([y_vals1,y_vals2])

x_vals = np.linspace(0.744511, 0.744576,dens)
y_vals = np.linspace(0.06841,0.06841,  dens)


#x_vals, y_vals = np.concatenate([x_vals1,x_vals2]), np.concatenate([y_vals1,y_vals2])


for i in range(dens):
    if i%500 == 0:
        print(100 * i / dens)
        print((time.time() - start_time)/60)
        
    my_x,my_y = x_vals[i],y_vals[i]
    
    xy = hMap_n(a_i,b,my_x,my_y,5000)
    if not (np.isnan(xy[0]) or (np.abs(xy[0])>100) or (np.abs(xy[1]) > 100)):
        x_conv[counter] = xy[0]
        y_conv[counter] = xy[1]
        counter += 1
    
        



     
#
fig = plt.figure(figsize = (8,8))
plt.title(str(b)+', '+str(a_i)+" Dens: "+str(dens))
#
ax = fig.add_subplot(1, 1, 1)  
#plt.xlim(-1.5,1.5)
#plt.ylim(-1.5,1.5)
ax.plot(x_conv[0:counter-1], y_conv[0:counter-1],'.',color='black')
#ax.plot(b_vals,a_vals,'.')
#for i in range(counter):
#    print(x_conv[i],y_conv[i])
  

print((time.time() - start_time)/60)