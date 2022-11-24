"""
file: da_sort.py
author: @jalbers
"""

from sys import stdin, stdout

n = int(stdin.readline())

for _ in range(n):
    a,b = (int(x) for x in stdin.readline().split())
    m = (b // 10) + 1
    if (b % 10) == 0:
        m = (b // 10) # number of lines to read
    num_list = []
    for _ in range(m):
        line = [int(x) for x in stdin.readline().split()]
        num_list += line
    sorted_num_list = num_list[:]
    sorted_num_list.sort()
    i = 0
    j = 0
    out_of_order = 0
    while i < b:
        if num_list[i] == sorted_num_list[j]:
            i += 1
            j += 1
        else:
            i += 1
            out_of_order += 1
    stdout.write(str(a) + " " + str(out_of_order)+"\n")

