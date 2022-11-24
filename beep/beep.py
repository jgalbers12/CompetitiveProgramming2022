# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 07:53:07 2022

@author: jgalb
"""

#taken mostly from geeksforgeeks

from sys import stdin
    
class beep:
    def __init__(self, cl):
        self.cl = cl
        self.n = len(self.cl)
        self.dist = [[401] * self.n for x in range(self.n)] 
        for i in range(len(self.cl)):
            for j in range(len(self.cl)):
                self.dist[i][j] = self.find_dist(self.cl[i], self.cl[j])
        self.dist[0][self.n-1] = 401
        self.dist[self.n-1][0] = 401
        self.start_mask = 2**self.n - 1
        self.min_list = [[-1] * self.n for _ in range(self.start_mask+1)]
        
    def find_dist(self, a, b):
        if a == b:
            return(0)
        else:
            return(abs(a[0] - b[0]) + abs(a[1] - b[1]))

    def find_min(self, mask, i):
        if self.min_list[mask][i] != -1:
            return(self.min_list[mask][i])
        m = 400
        if (1 << i | 1) == mask:
            return(self.dist[0][i])
        else:
            for j in range(1,self.n):
                if j != i and (mask & 1 << j):
                    m = min(m, self.find_min(mask & ~(1 << i), j) + self.dist[j][i])
            self.min_list[mask][i] = m
            return(m)

if __name__ == "__main__":
    for i in range(int(stdin.readline())):
        stdin.readline()
        cl = []
        start = [int(x) for x in stdin.readline().split()]
        cl.append(start)
        for j in range(int(stdin.readline())):
            c = [int(x) for x in stdin.readline().split()]
            cl.append(c)
        cl.append(start)
        if len(cl) == 2:
            print(0)
        else:
            m = beep(cl)
            ans = m.find_min(m.start_mask, m.n-1)
            print(ans)