# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 23:15:13 2021

@author: marce
"""


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import control.matlab as control
from scipy import signal

G11 = control.tf([0.4241],[148.6,1])
G12 = control.tf([-0.214],[4038.48,170.6,1])
G21 = control.tf([0.0695],[3326.4, 152.4,1])
G22 = control.tf([-0.5],[150,1])

print(G22)


T11=signal.TransferFunction(G11.num[0][0],G11.den[0][0])
print(T11)