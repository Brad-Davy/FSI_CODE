#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 17:11:00 2021

@author: bradleydavy
"""
import numpy as np
import matplotlib.pyplot as plt


def plot_graph():
    data = open('cd.txt','r').read().split('\n')
    
    dat = []
    x = []
    for eachline in data:
        dat.append(7*float(eachline.split()[1]))
        x.append(7*float(eachline.split()[0]))
    
    
    fig = plt.figure(figsize = (20,6))
    plt.plot(x,dat, color = 'black')
    plt.xlabel('$X$', fontsize=18)
    plt.ylabel('$Z$', fontsize=18)
    plt.savefig('Naca.eps', dpi = 600)
    plt.show()
    
def evaluate_z_bar():
    x = []
    y = []
    integral = []
    data = open('cd.txt','r').read().split('\n')
    for eachline in data:
        x.append(7*float(eachline.split()[1]))
        y.append(7*float(eachline.split()[0]))

    for i in range(1,int((len(x)-1)/2)):
        integral.append((x[i]**2-x[-(i+1)]**2)*0.05+(x[i-1]**2-x[-i]**2)*0.05/2)
        
    return sum(integral)*0.5
        
print(evaluate_z_bar()*2)
