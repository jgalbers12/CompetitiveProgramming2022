# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 11:54:50 2022

@author: jgalb
"""

from sys import stdin

def one(A):
    print(7)

def two(A):
    if A[0] > A[1]:
        print("Bigger")
    elif A[0] == A[1]:
        print("Equal")
    else:
        print("Smaller")

def three(A):
    sortedA = A[0:3]
    sortedA.sort()
    print(sortedA[1])

def four(A):
    print(sum(A))
    
def five(A):
    sum = 0
    for x in A:
        if x % 2 == 0:
            sum+=x
    print(sum)
    
def six(A):
    modA = map(lambda x: x % 26, A)
    alph = 'abcdefghijklmnopqrstuvwxyz'
    letters = []
    for num in modA:
        letters.append(alph[num])
    print(''.join(letters))

def seven(A):
    i = A[0]
    count = 0
    n = len(A)
    while True:
        if i == len(A) - 1:
            print("Done")
            break
        elif i >= len(A):
            print("Out")
            break
        else:
            if count > n:
                print("Cyclic")
                break
            count += 1
            i = A[i]
            
if __name__ == "__main__":
    f = [int(i) for i in stdin.readline().split()]
    nl = [int(j) for j in stdin.readline().split()]
    t = f[1]
    n = f[0]
    fun_dict = {1:one, 2:two, 3:three, 4:four, 5:five, 6:six, 7:seven}
    fun_dict[t](nl)
    