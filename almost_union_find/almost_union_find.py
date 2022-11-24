"""
created: 10/3/2022
author: @jalbers
"""

from sys import stdin,stdout

class AlmostUnionFind:
    def __init__(self, n):
        self.sum = [i for i in range(n)]
        self.nodes = [1] * n
        self.parent = [i for i in range(n)]
        self.child = [0] * n

    def find(self, u):
        while(u != self.parent[u]):
            prev_u = u
            self.nodes[self.parent[u]] += (self.nodes[u])
            self.nodes[u] = 0
            self.sum[self.parent[u]] += (self.sum[u])
            self.sum[u] = 0
            #prev_u = u
            (u, self.parent[u]) = (self.parent[u], self.parent[self.parent[u]]) # path splitting, not halving
            #u = self.parent[u] # u becomes grandparent
            #self.child[u] = self.parent[prev_u]
        self.child[u] = prev_u
        return u

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        root_1 = root_u
        root_2 = root_v
        if root_u != root_v:
            if self.nodes[root_u] < self.nodes[root_v]:
                root1 = root_v
                root_2 = root_u
            self.nodes[root_1] += self.nodes[root_2]
            self.nodes[root_2] = 0
            self.sum[root_1] += self.sum[root_2]
            self.sum[root_2] = 0
            self.parent[root_2] = root_1

    def move(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if self.child[v] != 0:
            self.parent[v] = self.child[v]
        else:

        """ if root_u != root_v:
            first_child = 0
            for i in range(len(self.parent)):
                if self.parent[i] == u and u != i:
                    first_child = i
                    break
            for i in range(first_child, len(self.parent)):
                if self.parent[i] == u and u != i:
                    self.parent[i] = first_child
            if root_u == u:
                self.parent[first_child] = first_child
                self.sum[first_child] = self.sum[u] - u
                self.nodes[first_child] = self.nodes[u] - 1
            else:
                self.parent[first_child] = root_u
            self.sum[root_v] += u
            self.sum[root_u] -= u
            self.sum[u] = 0
            self.nodes[root_v] += 1
            self.nodes[root_u] -= 1
            self.nodes[u] = 0
            self.parent[u] = root_v """

    def search(self, u):
        root_u = self.find(u)
        print(f"{self.nodes[root_u]} {self.sum[root_u]}")

if __name__ == "__main__":
    while(True):
        try:
            first_line = stdin.readline().split()
            n = int(first_line[0])
            m = int(first_line[1])
            p = AlmostUnionFind(n+1)
            for i in range(m):
                line = [int(x) for x in stdin.readline().split()]
                if line[0] == 1:
                    p.union(line[1], line[2])
                elif line[0] == 2:
                    p.move(line[1], line[2])
                    #print(f"parent: {p.parent}\nnode:{p.nodes}\nsum:{p.sum}\n")
                else:
                    p.search(line[1])
        except:
            break
