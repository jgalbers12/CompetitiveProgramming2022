# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 13:46:20 2022

@author: jgalb
"""

import math

maxint = 2**31-1

for n in range(20):
    if math.factorial(n) > maxint:
        print(n)
        break