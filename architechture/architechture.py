# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 21:00:22 2022

@author: jgalb
"""

from sys import stdin

if __name__ == "__main__":
    first_line = stdin.readline().split()
    r = first_line[0]
    c = first_line[1]
    r_list = stdin.readline().split()
    c_list = stdin.readline().split()
    if max(r_list) == max(c_list):
        print("possible")
    else:
        print("impossible")