# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 16:04:49 2022

@author: jgalb
"""
from sys import stdout
import random

n = 1000000

out = ""

for i in range(n):
    out += str(random.randint(1, 1000000)) + ' '

print(str(n))
print(out)