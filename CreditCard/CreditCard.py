# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 20:51:59 2022

@author: jgalb
"""

# r - interest rate, b - balance, m - amount paid monthly

from sys import stdin
import math

def normal_round(x):
    x = math.trunc(x + 0.5)
    #x = x * 10 ** -2
    return(x)

def compound(r, b, m):
    new_bal = (b * (1+(0.01 * r))) - m
    return(normal_round(new_bal))

def test(r:float, b:float, m:float):
    c = 0
    while(c<1200):
        b = compound(r, b, m)
        c+=1
        if int(b) <= 0:
            print(c)
            return
    print("impossible")
        
if __name__ == "__main__":
    n = int(stdin.readline())
    for i in range(n):
        ins = stdin.readline().split()
        ins[1] = float(ins[1]) * 100
        ins[2] = float(ins[2]) * 100
        test(float(ins[0]), ins[1], ins[2])
    

