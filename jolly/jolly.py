# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:02:58 2022

@author: jgalb
"""

from sys import stdin

def jolly(a):
    l = len(a)
    check_list = [False] * (l - 1)
    if len(a) == 1:
        print("Jolly")
    else:
        for i in range(l-1):
            diff = abs(a[i] - a[i+1])
            if diff != 0 and diff < l \
                and check_list[diff-1] == False:
                check_list[diff-1] = True
            else:
                print("Not jolly")
                return
        print("Jolly")

if __name__ == "__main__":
    for line in stdin:
        inl = [int(x) for x in line.split()]
        jolly(inl[1:])