"""
file: bulding_boundaries.py
author: @jgalb
"""

from itertools import permutations
from math import inf
from sys import stdin, stdout


class Boundaries:

    def __init__(self, b_list):
        self.b_list = b_list
        self.three = [[1,1,1], [1,1,0], [1,0,1], [0,1,1], [0,1,0], [0,0,1], [1,0,0], [0,0,0]]
        self.best = None
        self.configs = self.get_configs(self.b_list)

    def get_area(self):
        min = float(inf)
        for a in self.configs: # check side to side to side configs
            w = (a[0] + a[2] + a[4])
            h = max([a[1], a[3], a[5]])
            area = w * h
            if area < min:
                min = area
                self.best = a
        for a in self.configs:
            w = 0
            if a[3] <= a[1]:
                w = max([a[0] + a[2], a[4]])
            else:
                w = max([a[0] + a[2], a[4] + a[2]])
            h = max([a[1] + a[5], a[3]])
            area = w * h
            if area < min:
                min = area
                self.best = a
        return(min)

    def get_configs(self, l):
        arr = []
        perms = permutations([0,2,4], 3)
        t_list = self.three
        for p in perms:
            a, b, c = p
            for i in t_list:
                arr.append((l[a+i[0]], l[a+1-i[0]], l[b+i[1]], l[b+1-i[1]], l[c+i[2]], l[c+1-i[2]]))
        return arr
            
def main():
    for _ in range(int(stdin.readline())):
        b = Boundaries([int(x) for x in stdin.readline().split()])
        m = b.get_area()
        stdout.write(str(m)+"\n")

if __name__ == "__main__":
    main()