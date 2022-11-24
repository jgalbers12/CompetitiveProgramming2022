"""
title: acm.py
author: @jalbers
"""

from sys import stdin, stdout

class Potions:
    def __init__(self):
        self.parent = [i for i in range(500001)]
        self.num_ingredients = [1] * 500001

    def find(self, u):
        if (u != self.parent[u]):
            self.parent[u] = self.find(self.parent[u])
            return self.parent[u]
        else:
            return u

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.num_ingredients[root_u] > self.num_ingredients[root_v]:
                self.parent[root_v] = root_u
                self.num_ingredients[root_u] += self.num_ingredients[root_v]
            else:
                self.parent[root_u] = root_v
                self.num_ingredients[root_v] += self.num_ingredients[root_v]

    def check(self, ingredient_list):
        sets = set()
        for ingredient in ingredient_list:
            parent = self.find(ingredient)
            sets.add(parent)
        accum = 0
        for s in sets:
            accum += self.num_ingredients[s]
        if accum == len(ingredient_list):
            for i in range(len(ingredient_list)):
                self.union(ingredient_list[0],ingredient_list[i])
            sets.clear()
            return True
        else:
            return False

def main():
    n = int(stdin.readline())
    prob = Potions()
    count = 0
    for i in range(n):
        line = [int(x) for x in stdin.readline().split()]
        if prob.check(line[1:]):
            count += 1
    stdout.write(str(count))

if __name__ == "__main__":
    main()