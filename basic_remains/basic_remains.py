"""
file: basic_remains.py
author: @jalbers
"""

from sys import stdin, stdout

def to_base(x, b):
    if b == 10:
        return(str(x))
    s = ""
    while x > 0:
        s += str(x % b)
        x //= b
    s += str(x % b)
    s = s[::-1]
    for i in range(len(s)):
        if s[i] != "0":
            return(s[i:])
    return("0")


while True:
    line = stdin.readline().split()
    if line[0] != "0":
        b = int(line[0])
        p = int(line[1], b)
        m = int(line[2], b)
        a = p % m
        stdout.write(to_base(a, b)+"\n")
    else:
        break