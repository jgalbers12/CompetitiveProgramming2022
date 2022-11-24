"""
file: blackboard_numbers.py
author: @jalbers
"""

from sys import stdin,stdout
import math

def get_nums(x):
    bases = [2,8,10,16]
    nums = [None, None, None, None]
    for i in range(4):
        try:
            num = int(x, bases[i])
        except:
            pass
        else:
            nums[i] = num
    return nums

def check_prime(x):
    if x == 1:
        return False
    if x % 2 == 0 and x != 2:
        return False
    for i in range(3, int(math.sqrt(x))+1, 2):
        if x % i == 0:
            return False
    return True

t = int(stdin.readline())

for _ in range(t):
    numbers = get_nums(stdin.readline().rstrip())
    numer = 0
    denom = 0
    for n in numbers:
        if n != None:
            denom += 1
            if check_prime(n):
                numer += 1
    if numer == 0:
        denom = 1
    elif denom % numer == 0:
        denom = denom // numer
        numer = 1
    stdout.write(f"{numer}/{denom}\n")

