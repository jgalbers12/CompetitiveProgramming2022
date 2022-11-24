"""
file: eating_everything2.py
author: @jalbers
"""

from sys import stdin, stdout

n, e = (int(x) for x in stdin.readline().split()) # number of nodes, edges
s = [int(x) for x in stdin.readline().split()] # score list
graph = {i: [] for i in range(n)}

def connect(a,b):
    graph[a].append(b)

for _ in range(e):
    i, j = [int(x) for x in stdin.readline().split()]
    connect(i, j)

f = [0] * n # max score for path starting at i-th node
v = [False] * n # visited array

def dfs(x):
    v[x] = True
    if graph[x]: # not at sink
        for w in graph[x]:
            if not v[w]:
                dfs(w)
            f[x] = max(f[x], f[w], s[x] + 0.5*f[w])
            #print(f"x: {x}, w: {w}, f[x]: {f[x]} \n")
    else: # at sink
        f[x] = s[x]

dfs(0) # 0 is source
m = max(f)
stdout.write(str(m))