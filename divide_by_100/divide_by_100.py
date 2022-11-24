# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 15:50:41 2022

@author: jgalb
"""

from sys import stdin,stdout

zero_list = ['0'] * 10**6

def divide(n, m): # n/m
    l_m = len(m)
    l_n = len(n)
    new_num = ""
    if l_n < l_m: # 0._ case
        new_num = "0."
        new_num += ''.join(zero_list[0:(l_m-l_n)-1])
        new_num += n
    else:
        diff = l_n - l_m
        new_num = n[0:diff+1] + "." + n[diff+1:]
    if new_num[-1] == '.':
        new_num = new_num[0:-1]
    else:
        for i in range(len(new_num)-1, -1, -1):
            if new_num[i] != '0':
                if new_num[i] == '.':
                    new_num = new_num[0:i]
                    break
                else:
                    new_num = new_num[0:i+1]
                    break
    return(new_num)

if __name__ == "__main__":
    n = stdin.readline().rstrip()
    m = stdin.readline().rstrip()
    stdout.write(divide(n,m))
    
        