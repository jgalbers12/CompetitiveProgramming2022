# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:15:13 2022

@author: jgalb
"""

from sys import stdin

class baloon:
    def __init__(self, s):
        self.s = s
        self.n = len(s)
        self.b_list = [0]*(10**6+1)
        
    def search(self):
        for i in range(self.n):
            x = self.s[i]
            self.b_list[x] += 1
            if self.b_list[x+1] != 0:
                self.b_list[x+1] -= 1

if __name__ == "__main__":
    n = int(stdin.readline())
    s = [int(i)-1 for i in stdin.readline().split()]
    #print('in time: ', stop - start)
    #start = timeit.default_timer()
    prob = baloon(s)
    #stop = timeit.default_timer()
    #print('class time: ', stop - start)
    #start = timeit.default_timer()
    prob.search()
    #stop = timeit.default_timer()
    #print('loop time: ', stop - start) 
    #start = timeit.default_timer()
    print(sum(prob.b_list))
    #stop = timeit.default_timer()
    #print('Sum time: ', stop - start) 
    