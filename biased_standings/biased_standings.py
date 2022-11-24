"""
file: biased_standing.py
author: @jalbers
"""

from sys import stdin, stdout

n = int(stdin.readline())

for i in range(n):
    stdin.readline()
    m = int(stdin.readline())

    rankings = [-1] * m
    current_index = 0
    bias = 0

    for j in range(m):
        line = stdin.readline().split()
        rankings[j] = int(line[1])

    rankings.sort()

    while current_index < m:
        r = rankings[current_index]
        bias += abs(r - (current_index + 1))
        current_index += 1

    stdout.write(str(bias)+"\n")