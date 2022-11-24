
from sys import stdin, stdout

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0 for i in range(n+1)]

    def find(self, u):
        while(u != self.parent[u]):
            (u, self.parent[u]) = (self.parent[u], self.parent[self.parent[u]])
        return u

    def union(self, u, v):
        root_1 = self.find(u)
        root_2 = self.find(v)
        if root_1 != root_2:
            if self.rank[root_1] < self.rank[root_2]:
                (root_1, root_2) = (root_2, root_1)
            self.parent[root_2] = root_1
            self.rank[root_1] += 1

if __name__ == "__main__":
    first_line = stdin.readline().split()
    q = int(first_line[0])
    n = int(first_line[1])
    prob = UnionFind(q)
    for _ in range(n):
        line = stdin.readline().split()
        o = line[0]
        (u, v) = (int(x) for x in line[1:])
        if o == "?":
            if prob.find(u) == prob.find(v):
                stdout.write("yes\n")
            else:
                stdout.write("no\n")
        else:
            prob.union(u,v)

