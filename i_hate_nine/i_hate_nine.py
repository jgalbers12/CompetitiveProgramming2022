"""
file: i_hate_nine.py
author: @jalbers
"""

from sys import stdin, stdout

def no_nines(d):
    if d == 1:
        return(8)
    return((pow(9, d-1, 1000000007) * 8) % 1000000007)

n = int(stdin.readline())
for _ in range(n):
    d = int(stdin.readline())
    stdout.write(str(no_nines(d))+"\n")
