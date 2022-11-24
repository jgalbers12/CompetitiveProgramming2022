# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 20:11:39 2022

@author: jgalb
"""

from sys import stdin, stdout

def hash_string(string):
    ans = 0
    for c in string:
        ans = ans ^ ord(c)
    return(ans)
    
def compare(s1, s2):
    if len(s1) == len(s2):
        i = 0
        while (i < len(s1)):
            if s1[i] == s2[i]:
                if i == len(s1) - 1:
                    return(True)
                i += 1
            else: break
    return(False)

while(True):
    n = int(stdin.readline())
    if n != 0:
        string_list = [None] * n
        hash_list = [None] * n
        unique = [True] * n
        n_unique = n
        collisions = 0
        for i in range(n):
            line = stdin.readline()
            string_list[i] = line
            hash_list[i] = hash_string(line)
        for j in range(n-1):
            for k in range(j+1,n):
                if hash_list[j] == hash_list[k]:
                    if compare(string_list[j], string_list[k]):
                        if unique[k]:
                            unique[k] = False
                            n_unique -= 1
                    else:
                        collisions += 1
        stdout.write(f"{n_unique} {collisions}")
        stdout.write("\n")
    else:
        break
            
        
    
    