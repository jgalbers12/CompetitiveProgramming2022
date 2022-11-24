"""
file: dance_recital.py
author: @jalbers
"""

from itertools import permutations
from math import factorial
from sys import stdin, stdout

class Recital:
    def __init__(self, n):
        self.n = n
        self.schedule = [0] * n
        self.order = [i for i in range(self.n)]
        self.min = 10000000
        self.graph = [[-1] * n for _ in range(n)]

    def char_to_index(self, c):
        return(ord(c) - ord("A"))

    def insert(self, dancer, routine):
        self.schedule[routine] = self.schedule[routine] | 1 << self.char_to_index(dancer)

    def fill_graph(self):
        for i in range(self.n-1):
            for j in range(i + 1, self.n):
                if i != j:
                    count = 0
                    result = self.schedule[i] & self.schedule[j]
                    for k in range(26):
                        if result & 1 << k:
                            count += 1
                    self.graph[i][j] = count
                    self.graph[j][i] = count

    def swap(self, a, b):
        (self.order[a], self.order[b]) = (self.order[b], self.order[a])
    
    def find_quicks(self, i):
        d = 0
        if i == self.n:
            for j in range(self.n-1):
                d += self.graph[self.order[j]][self.order[j+1]]
            if d < self.min:
                self.min = d
        else:
            for j in range(i, self.n):
                self.swap(i,j)
                self.find_quicks(i+1)
                self.swap(i,j)

def main():
    n = int(stdin.readline())
    r = Recital(n)
    for i in range(n):
        line = stdin.readline().rstrip()
        for c in line:
            r.insert(c, i)
    r.fill_graph()
    r.find_quicks(0)
    stdout.write(str(r.min))

if __name__ == "__main__":
    main()
