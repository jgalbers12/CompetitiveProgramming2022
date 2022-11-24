"""
file: gepetto.py
author: @jgalb
"""
from sys import stdin, stdout
from itertools import combinations, combinations_with_replacement, permutations

n, m = (int(x) for x in stdin.readline().split())

bit_strings = set()

def generate_all(i, n, s):
    if i == n:
        bit_strings.add(s)
        return
    s += "0"
    generate_all(i+1, n, s)
    s = s[:-1] + "1"
    generate_all(i+1, n, s)

generate_all(0, n, "")



def check(c, a, b):
    if c[a-1] == "1" and c[b-1] == "1":
        return False
    else:
        return True

for _ in range(m):
    a, b = (int(x) for x in stdin.readline().split())
    remove_list = []
    for c in bit_strings:
        if not check(c, a, b):
            remove_list.append(c)
    for x in remove_list:
        bit_strings.remove(x)

stdout.write(str(len(bit_strings)))