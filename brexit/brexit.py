"""
file: brexit.py
author: @jalbers
"""

from sys import stdin, stdout
from collections import deque

class Countries:
    def __init__(self, n, c, l):
        self.n = n
        self.c = c
        self.l = l
        self.graph = {x:[] for x in range(n)}
        self.visited = [False] * n
        self.leaving = [False] * n
        self.num_adj_leaving = [0] * n
        self.num_adj = [0] * n
        self.leaving[l] = True

    def connect(self, i, j):
        self.graph[i].append(j)
        self.graph[j].append(i)
        self.num_adj[i] += 1
        self.num_adj[j] += 1

    def search(self):
        i = self.l
        next = deque()
        while(True):
            self.visited[i] = True
            for neighbor in self.graph[i]:
                self.num_adj_leaving[neighbor] += 1
                if self.num_adj_leaving[neighbor]*2 >= self.num_adj[neighbor]:
                    self.leaving[neighbor] = True
                    if self.visited[neighbor] == False:
                        next.append(neighbor)
            if next:
                i = next.pop()
            else:
                break
        

    def find_ans(self):
        self.search()
        return(self.leaving[self.c])

def main():
    line0 = [int(x) for x in stdin.readline().split()]
    n = line0[0]
    p = line0[1]
    c = line0[2]
    l = line0[3]
    prob = Countries(n, c-1, l-1)
    for _ in range(p):
        i, j = [int(x) for x in stdin.readline().split()]
        prob.connect(i-1, j-1)
    ans = prob.find_ans()
    #print(prob.leaving)
    if ans:
        stdout.write("leave")
    else:
        stdout.write("stay")

if __name__ == "__main__":
    main()
