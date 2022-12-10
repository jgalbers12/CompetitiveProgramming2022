"""
file: grid.py
author: @jalbers
kattis: grid
"""

from sys import stdin, stdout
from math import inf

r, c = [int(x) for x in stdin.readline().split()]
grid = []

for _ in range(r):
    line = stdin.readline()
    row = [int(line[x]) for x in range(c)]
    grid.append(row)

#print(grid)
min_dist_list = [[inf]*c for _ in range(r)]
min_dist_list[0][0] = 0
in_set = [[False]*c for _ in range(r)]
x,y = 0,0
in_set[0][0] = True
next_set = set()

def neighbors(i, j):
    val = grid[i][j]
    return([(i+a[0],j+a[1]) for a in [(val,0),(0,val), \
        (-val,0), (0,-val)] if ((0 <= i+a[0] < r) and (0 <= j+a[1] < c))])

while True:
    dist_to_n = min_dist_list[x][y] + 1
    #print(f"neighbors({x}, {y}):{neighbors(x,y)}")
    for a,b in neighbors(x, y):
        #print(f"x: {x} y: {y} a: {a} b: {b}")
        if not in_set[a][b]:
            #print(f"add {a} {b}")
            next_set.add((a,b))
            if dist_to_n < min_dist_list[a][b]:
                min_dist_list[a][b] = dist_to_n
    min_next = inf
    next_x = None
    next_y = None
    if next_set:
        #print(f"x: {x} y: {y} next_set: {next_set}")
        for nx, ny in next_set:
            if min_dist_list[nx][ny] < min_next:
                #print(f"x: {x}, y: {y}, c: {c}, d: {d}")
                min_next = min_dist_list[nx][ny]
                next_x = nx
                next_y = ny
        in_set[next_x][next_y] = True
        next_set.remove((next_x,next_y))
        x = next_x
        y = next_y
    else:
        break

if in_set[r-1][c-1]:
    stdout.write(str(min_dist_list[r-1][c-1]))
else:
    stdout.write(str(-1))