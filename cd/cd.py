# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 15:50:31 2022

@author: jgalb
"""

from sys import stdin

def listify(m_list, n_list, max_m, max_n):
    count = 0
    m_bin_list = [False] * max_m
    n_bin_list = [False] * max_n
    for item in m_list:
        m_bin_list[item - 1] = True
    for item in n_list:
        n_bin_list[item - 1] = True
    if max_m <= max_n:
        for i in range(max_m):
            if m_bin_list[i] == n_bin_list[i]:
                count += 1
    else:
        for j in range(max_n):
            if m_bin_list[j] == n_bin_list[j]:
                count += 1
    print(count)


    
if __name__ == "__main__":
#with open('cd_test.txt', 'r') as f:
    first_line = stdin.readline().split()
    m = int(first_line[0])
    n = int(first_line[1])
    m_list = []
    n_list = []
    max_n = 0
    max_m = 0
    for i in range(m):
        #x = int(f.readline())
        x = int(stdin.readline())
        m_list.append(x)
        if x > max_m:
            max_m = x
    for j in range(n):
        #y = int(f.readline())
        y = int(stdin.readline())
        n_list.append(y)
        if y > max_n:
            max_n = y
    #print(m_list, n_list)
    listify(m_list, n_list, max_m, max_n)
        
"""for i in range(m):
     index = stdin.readline()
     m_list[index] = True
 for j in range(n):
     index = stdin.readline()
     n_list[index] = True"""