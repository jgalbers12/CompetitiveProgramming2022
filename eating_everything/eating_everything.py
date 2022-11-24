"""
file: eating_everything.py
author: @jalbers
"""

from sys import stdin, stdout

class Eat:

    def __init__(self, n, scores):
        self.n = n
        self.graph = {i: [] for i in range(self.n)}
        self.scores = scores
        self.max = [-1] * self.n
        self.ate = [[]] * self.n
        self.visited = [set()] * self.n
        self.max[0] = (self.scores[0])
        self.ate[0] = [0]
        self.visited[0].add(0)

    def connect(self, i, j):
        self.graph[i].append(j)

    def mult(self, x, k):
        return(x/(2**(k-1)))

    def find_max(self, i, ate_last):#, visited):
        #visited.add(i)
        #print(f"i:{i}, {visited}")
        m = self.scores[i]
        k = i
        for j in ate_last:
            if j != i:
                cur = self.mult(self.scores[i], len(self.ate[j])+1) + self.max[j]
                if cur > m:
                    k = j
                    m = cur
        if k == i:
            self.ate[i] = [i]
        else:
            self.ate[i] = self.ate[k].copy()
            self.ate[i].append(i)
        self.max[i] = m
        for j in self.graph[i]:
            if j not in self.visited[i]:
                self.visited[j].extend(self.visited[i])
                self.find_max(j, self.ate[i], visited)

    def find_answer(self):
        return(max(self.max))

def main():
    n, e = (int(x) for x in stdin.readline().split())
    s = [int(x) for x in stdin.readline().split()]
    prob = Eat(n, s)
    for _ in range(e):
        i, j = [int(x) for x in stdin.readline().split()]
        prob.connect(i, j)
    prob.find_max(0, [0], set())
    stdout.write(str(prob.find_answer()))

if __name__ == "__main__":
    main()
