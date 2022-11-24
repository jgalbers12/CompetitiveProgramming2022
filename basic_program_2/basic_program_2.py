# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 08:59:01 2022

@author: jgalb
"""

from sys import stdin

def one(A):
    A.sort()
    i = 0
    j = len(A)-1
    while(i!=j):
        if A[j] >= 7777:
            j -= 1
        elif A[j] + A[i] > 7777:
            j -= 1
        elif A[j] + A[i] < 7777:
            i += 1
        else: 
            print("Yes")
            return
    print("No")
    # for i in range(len(A)-1):
    #     x = A[i]
    #     for j in range(i+1, len(A)):
    #         y = A[j]
    #         if x + y == 7777 and x != y:
    #             print("Yes")
    #             return
    # print("No")

def two(A):
    A.sort()
    for i in range(len(A)-1):
        x = A[i]
        y = A[i+1]
        if x == y:
            print("Contains duplicate")
            return
    print("Unique")

def three(A):
    A.sort()
    count = 1
    for i in range(len(A)-1):
        if A[i+1] == A[i]:
            count+=1
            if count > len(A)/2:
                print(A[i])
                return
        else:
            count = 1
    print(-1)

def four(A):
    A.sort()
    length = len(A)
    if len(A) % 2 == 0:
        print(f"{A[(length//2) - 1]} {A[length//2]}")
    else: print(A[length//2])

def five(A):
    A.sort()
    val_list = []
    for val in A:
        if val >= 100 and val <= 999:
            val_list.append(val)
    val_list = [str(x) for x in val_list]
    print(" ".join(val_list))
    
                
if __name__ == "__main__":
    (n, t) = stdin.readline().split()
    A = [int(i) for i in stdin.readline().split()]
    fun_dict = {1:one, 2:two, 3:three, 4:four, 5:five}
    fun_dict[int(t)](A)