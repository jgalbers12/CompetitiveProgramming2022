"""
file: dominoes_2.py
author: @jalbers
kattis: Dominoes 2
"""

from sys import stdin, stdout

class Dominoes:
    def __init__(self, n):
        self.n = n
        self.graph = {x:[] for x in range(n)}
        self.visited = [False] * n

    def connect(self, i, j):
        self.graph[i].append(j)

    def dfs(self, i):
        self.visited[i] = True
        for node in self.graph[i]:
            if self.visited[node] == False:
                self.dfs(node)

    def find_ans(self):
        return(sum(self.visited))


def main():
    p = int(stdin.readline())
    for _ in range(p):
        n, m, l = [int(x) for x in stdin.readline().split()]
        prob = Dominoes(n)
        for _ in range(m):
            i, j = [int(x) for x in stdin.readline().split()]
            prob.connect(i-1, j-1)
        for _ in range(l):
            d = int(stdin.readline())
            prob.dfs(d-1)
        stdout.write(f"{prob.find_ans()}\n")

if __name__ == "__main__":
    main()