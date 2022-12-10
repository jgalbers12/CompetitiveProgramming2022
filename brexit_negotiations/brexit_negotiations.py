"""
file: brexit_negotiations.py
author: @jalbers
"""

from sys import stdin, stdout

class Negotiations:
    def __init__(self, n):
        self.n = n
        self.graph = {x:[] for x in range(n)}
        self.length = [0] * n
        self.rank = [-1] * n
        self.num = 0
        self.length_node = []

    def connect(self, i, j):
        self.graph[i].append(j)

    def zip_length_sort(self):
        self.length_node = list(zip(self.length, [x for x in range(self.n)]))
        self.length_node.sort(reverse=True) # descending order of length

    def sort(self): # reverse topological ordering
        for _, node in self.length_node: # dfs from highest length node
            if self.rank[node] == -1:
                self.dfs(node)

    def dfs(self, i):
        for node in self.graph[i]:
            if self.rank[node] == -1:
                self.dfs(node)
        self.rank[i] = self.num
        self.num += 1


    def find_ans(self):
        self.zip_length_sort()
        self.sort()
        return(max(self.length[i] + self.rank[i] for i in range(self.n)))

def main():
    n = int(stdin.readline())
    prob = Negotiations(n)
    for i in range(n):
        line = [int(x) for x in stdin.readline().split()]
        prob.length[i] = line[0]
        for j in range(line[1]):
            prob.connect(i, line[j+2]-1)
    stdout.write(str(prob.find_ans()))

if __name__ == "__main__":
    main()