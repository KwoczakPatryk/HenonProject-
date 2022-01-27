#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 22:55:19 2022

@author: patrykkwoczak
"""
import numpy as np
import matplotlib.pyplot as plt
import imageio
import os

def hMap(a,b,x,y):
    return 1 - a*x**2 + b*y
    

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
        if np.abs(x_i) > 200 or np.abs(y_i) > 200 :
            
            break
        
    x_n, y_n = x_i,y_i
    return [x_n, y_n]

xy1 = [0.7405849810673275,0]
xy2 = [0.740605008328963,0]

filenames = []
for i in range(50):
    fig = plt.figure(figsize = (8,8))
    plt.title('Orbit Tracker, '+str(i))
    ax = fig.add_subplot(1,1,1)
    plt.xlim(-0.3,1)
    plt.ylim(-0.3,1)
    xy1_i = hMap_n( 2.2534022522522523,-0.43206301601601604,xy1[0],0,i)
    xy2_i = hMap_n( 2.253492342342342,-0.43211343443443445,xy2[0],0,i)
    ax.plot([xy1_i[0]],[xy1_i[1]],'x',color='red')
    ax.plot([xy2_i[0]],[xy2_i[1]],'x',color='blue')
    filename = f'{i}.png'
    filenames.append(filename)
    plt.savefig(filename)
    plt.close()

with imageio.get_writer('HenonOrbitPlot1.gif',mode = 'I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

for filename in set(filenames):
    os.remove(filename)
print('done')