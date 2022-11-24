# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 23:16:49 2022

@author: jgalb
"""

from sys import stdin

class dfs:
    def __init__(self,d): # takes dict of nodes and edge nums
        self.d = d
        self.n = len(self.d)
        self.mask = 1 # first node visited
        self.all_visited = 2**self.n - 1
        self.g = self.make_graph()
        self.sub = [] # sub graph solution
    
    def make_graph(self): # find connections between nodes
        g = dict(zip(range(self.n), [[] for _ in range(self.n)]))
        for i in range(self.n):
            self.d[i].sort()
        for j in range(self.n-1):
            j_len = len(self.d[j])
            for k in range(j+1, self.n):
                k_len = len(self.d[k])
                j_i = 0
                k_i = 0
                while(j_i < j_len and k_i < k_len):
                    j_val, k_val = self.d[j][j_i], self.d[k][k_i]
                    if j_val == k_val: # val in both edge sets add nodes to each others lists
                        g[k].append((j,j_val))
                        g[j].append((k,k_val))
                        break # only need one connection for a pair
                    elif j_val < k_val:
                        j_i += 1
                    else:
                        k_i += 1
        #     j_list = [False] * 10**9
        #     for val in self.d[j]:
        #         j_list[val] = True
        #     for k in range(j+1, self.n):
        #         k_list = [False] * 10**9
        #         for val in k_list:
        #             k_list[val] = True
        #         for val in self.d[j]:
        #             if k_list[val] == j_list[val]:
        #                 g[j].append((k, val))
        #                 g[k].append((j,val))
        #                 break
        return(g)
    
    def search(self, v): # dfs of graph
        if (self.mask & self.all_visited == self.all_visited):
            return
        for neigh in self.g[v]:
            if ((1 << neigh[0]) & self.mask) == 0:
                self.sub.append((v, neigh[0], neigh[1]))
                self.mask = self.mask | (1 << neigh[0])
                self.search(neigh[0])
            
            

d = {}
for i in range(int(stdin.readline())):
     w = [int(x) for x in stdin.readline().split()]
     d[i] = w[1:]
a = dfs(d)
a.search(0)
if len(a.sub) == a.n-1:
    for e in a.sub:
        print(f"{e[0]+1} {e[1]+1} {e[2]}")
else:
    print("impossible")