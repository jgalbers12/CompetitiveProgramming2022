# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 16:31:58 2022

@author: jgalb
"""

from sys import stdin

def move_cow(a, b, ag, bg, at, bt):
    cow_a_to_ag = abs(a) + abs(ag-a)
    cow_b_to_bg = abs(ag-b) + abs(bg-b)
    cow_b_to_a = abs(b) + abs(a - b)
    cow_b_to_bg_if_moved = abs(ag-a) + abs(bg-a)
    if (cow_a_to_ag <= at) & \
        (((cow_a_to_ag + cow_b_to_bg) <= bt) \
         or ((cow_b_to_a + abs(ag-a) + cow_b_to_bg_if_moved) <= bt)): \
            return(True)
    else:
        return(False)
        
if __name__ == "__main__":
    line1 = stdin.readline().split()
    line2 = stdin.readline().split()
    line3 = stdin.readline().split()
    m, n = int(line1[0]), int(line1[1])
    mg, ng = int(line2[0]), int(line2[1])
    mt, nt = int(line3[0]), int(line3[1])
    if (move_cow(m, n, mg, ng, mt, nt) or move_cow(n, m, ng, mg, nt, mt)):
        print("possible")
    else: print("impossible")