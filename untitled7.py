# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 23:35:48 2021

@author: marce
"""

from scipy import signal
import control.matlab as control
import matplotlib.pyplot as plt
import sympy as sym
import simpy as sp

#Función de transferencia Yt
num1 = [0.4241]
den1 = [148.6, 1]
G11 = signal.TransferFunction(num1, den1)

num2 = [-0.214]
den2 = [4038.48, 170.6, 1]
G21 = signal.TransferFunction(num2, den2)

num3 = [0.0695]
den3 = [3326.4, 152.4, 1]
G12 = signal.TransferFunction(num3, den3)

num4 = [-0.5]
den4 = [150, 1]
G12 = signal.TransferFunction(num4, den4)

# Matriz de Funciones de transferencia
numG= [[num1, num3], [num2, num4]]
denG = [[den1, den3], [den2, den4]]
Gtf= control.TransferFunction(numG, denG)
Gtf

#Representación en espacio de estados
Gss = control.tf2ss(Gtf)
Gss