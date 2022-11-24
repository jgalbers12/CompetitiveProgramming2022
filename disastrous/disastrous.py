# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 13:42:28 2022

@author: jgalb
"""

from sys import stdin
import math

def find_max(A):
    end_stamps = []
    i = 0
    count = 0
    max_count = 0
    length = len(A)
    while(i<length):
        if len(end_stamps) == 0 or A[i] < end_stamps[0]:
            count+=1
            end_stamps.append(A[i]+1000)
            i+=1
            if count > max_count:
                max_count = count
        else:
            end_stamps.pop(0)
            count-=1
    return(max_count)

if __name__ == "__main__":
    (n, s) = stdin.readline().split()
    times = []
    for i in range(int(n)):
        times.append(int(stdin.readline()))
    print(math.ceil(find_max(times)/int(s)))