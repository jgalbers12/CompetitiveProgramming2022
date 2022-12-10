"""
file: breaking_bad.py
author: @jalbers
kattis: Breaking Bad
"""

from sys import stdin, stdout, setrecursionlimit
from collections import deque

class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = {}
        self.num = 0
        self.visited = [False] * n
        self.coloring = {}
        self.valid = True

    def add(self, name):
        self.graph[name] = []
        self.coloring[name] = None

    def connect(self, name1, name2):
        self.graph[name1].append(name2)
        self.graph[name2].append(name1)

    def dfs(self, i, color):
        if self.valid == False:
            return
        color = not color
        self.coloring[i] = color
        for node in self.graph[i]:
            if self.coloring[node] == None:
                self.dfs(node, color)
            elif self.coloring[node] == color:
                self.valid = False
                return
    
    def find_ans(self):
        color0 = []
        color1 = []
        s0 = ""
        s1 = ""
        for name in self.coloring.keys():
            if self.coloring[name] == None:
                self.dfs(name, True)
        if self.valid:
            for name in self.coloring.keys():
                if self.coloring[name]:
                    color1.append(name)
                else:
                    color0.append(name)
            s0 = " ".join(color0)
            s1 = " ".join(color1)
            stdout.write(s0+"\n")
            stdout.write(s1)
        else:
            stdout.write("impossible")

def main():
    setrecursionlimit(100000)
    n = int(stdin.readline())
    prob = Graph(n)
    for _ in range(n):
        prob.add(stdin.readline().rstrip())
    m = int(stdin.readline())
    for _ in range(m):
        i, j = stdin.readline().rstrip().split()
        prob.connect(i, j)
    prob.find_ans()

if __name__ == "__main__":
    main()