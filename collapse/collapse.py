"""
file: collapse.py
author: @jalbers
"""

from sys import stdin, stdout
from collections import deque

class Island:

    def __init__(self, n):
        self.n = n
        self.graph = {x:[] for x in range(n)}
        self.t = [0] * n # min sum of weights to node needed to stay alive
        self.current = [0] * n # sum of edges to each node
        self.alive = [True] * n # keep track of nodes that are alive
        self.visited = [False] * n # keep track of nodes that have been visited
        self.alive[0] = False

    def connect(self, x, y, val):
        self.graph[x].append((y, val))
        self.current[y] += val

    def dfs(self):
        next = deque()
        v = 0
        while(True):
            self.visited[v] = True
            for node, val in self.graph[v]: # for each node where edge from v to node
                self.current[node] -= val # subtract weight of edge to node from current sum
                if self.current[node] < self.t[node]:
                    self.alive[node] = False
                    if self.visited[node] == False:
                        next.append(node)
            if next:
                v = next.pop()
            else:
                break

    def find_ans(self):
        return(sum(self.alive))

def main():
    n = int(stdin.readline())
    prob = Island(n)
    for i in range(n):
        line = [int(x) for x in stdin.readline().rstrip().split()]
        prob.t[i] = line[0]
        for j in range(line[1]):
            prob.connect(line[j*2 + 2]-1, i, line[j*2 + 3])
    prob.dfs()
    stdout.write(str(prob.find_ans()))

if __name__ == "__main__":
    main()
    