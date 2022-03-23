# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 01:17:26 2021

@author: marce
"""

from scipy import signal
import control.matlab as control
import matplotlib.pyplot as plt
import sympy as sym
import simpy as sp
import numpy as np

#Función de transferencia Yt
num1 = [0.4241]
den1 = [148.6, 1]
G11 = signal.TransferFunction(num1, den1)

num2 = [-0.214]
den2 = [4038.48, 170.6, 1]
G12 = signal.TransferFunction(num2, den2)

num3 = [0.0695]
den3 = [3326.4, 152.4, 1]
G21 = signal.TransferFunction(num3, den3)

num4 = [-0.5]
den4 = [150, 1]
G22 = signal.TransferFunction(num4, den4)

# Matriz de Funciones de transferencia
numG= [[num1, num2], [num3, num4]]
denG = [[den1, den2], [den3, den4]]
Gtf= control.TransferFunction(numG, denG)
Gtf

#Representación en espacio de estados
Gss = control.tf2ss(Gtf)
Gss
 #Vector propio matriz A
x = np.linalg.eig(Gss.A)

#Ubicación de polos del controlador Kp
p = [0, -60, -70, -90, -100, -110]
Kp =control.place(Gss.A, Gss.B, p)
Kp

#Modificación Matriz A y B por el controlador Kp
A1 = Kp*Gss.A
B1 = Kp*Gss.B