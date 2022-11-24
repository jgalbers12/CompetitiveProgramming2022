"""
file: air_conditioned.py
author: @jalbers
"""

from sys import stdin, stdout

n = int(stdin.readline())

temps = [(None,None)] * n
num_temps = 1

for i in range(n):
    l, u = [int(x) for x in stdin.readline().split()]
    temps[i] = (u,l)


temps.sort()
current = temps[0][0]
for j in range(n):
    if temps[j][1] > current:
        current = temps[j][0]
        num_temps += 1

stdout.write(str(num_temps))