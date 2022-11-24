"""
file: sqaure_deal.py
author: @jgalb
"""

from itertools import permutations
from math import inf
from sys import stdin, stdout


class SquareDeal:

    def __init__(self, b_list):
        self.b_list = b_list
        self.three = [[1,1,1], [1,1,0], [1,0,1], [0,1,1], [0,1,0], [0,0,1], [1,0,0], [0,0,0]]
        self.configs = self.get_configs(self.b_list)

    def check(self):
        for a in self.configs: # check side to side to side configs
            h = (a[1] + a[3] + a[5])
            if h == a[0] == a[2] == a[4]:
                return True
        for a in self.configs:
            if a[3] == a[5] and a[0] == a[2] + a[4] and a[1] + a[3] == a[0]:
                return True
        return False

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
    rectangles = []
    for line in stdin:
        a,b = (int(x) for x in line.split())
        rectangles.append(a)
        rectangles.append(b)
    sd = SquareDeal(rectangles)
    if sd.check():
        stdout.write("YES")
    else:
        stdout.write("NO")

if __name__ == "__main__":
    main()