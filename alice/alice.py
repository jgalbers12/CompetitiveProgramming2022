"""
file: alice.py
author: @jalbers
"""

from sys import stdin, stdout

for _ in range(int(stdin.readline())):

    (n, m) = (int(x) for x in stdin.readline().split())
    arr = [int(x) for x in stdin.readline().split()]

    current_sum = 0
    best = 0
    before_m = 0
    after_m = 0
    m_in = False
    for i in range(n):
        if arr[i] == m:
            c = before_m + after_m + m
            if c > best:
                best = c
            if m_in:
                before_m = after_m
                after_m = 0
            else:
                m_in = True
        elif arr[i] > m:
            if m_in:
                after_m += arr[i]
            else:
                before_m += arr[i]
        else:
            if m_in:
                c = before_m + after_m + m
                if c > best:
                    best = c
            before_m = 0
            after_m = 0
            m_in = False

    if m_in:
        c = before_m + after_m + m
        if c > best:
            best = c
        

    # cur = 0
    # best = 0
    # for j in range(len(sum_arr)-1):
    #     cur = sum_arr[j] + sum_arr[j+1] + m
    #     if cur > best:
    #         best = cur

    stdout.write(str(best)+"\n")