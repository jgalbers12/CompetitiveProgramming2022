# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 15:23:01 2022

@author: jgalb
"""

from sys import stdin,stdout

r_dict = {"@":["at", "At"], "&":["and", "And"], "1":["one", "One","won", "Won"], "2":["to", "To","too", "Too","two", "Two"], \
          "b":["bea","be","bee"], "B":["Bea","Be","Bee"],"c":["sea","see"], "C":["Sea","See"], "i":["eye"], "I":["Eye"], "o":["oh","owe"],"O":["Oh","Owe"], \
              "r":["are"], "R":["Are"],"u":["you"], "U":["You"], "y":["why"], "Y":["Why"]}
    
start_list = [False] * 123 
ord_list = [[] for i in range(123)]

for key in r_dict:
    for word in r_dict[key]:
        for j in range(len(word)):
            if j == 0:
                ord_list[ord(word[j])].append((-1, ord(word[j+1])))
            elif j == len(word) - 1:
                ord_list[ord(word[j])].append((ord(word[j-1]), key))
            else:
                ord_list[ord(word[j])].append((ord(word[j-1]), ord(word[j+1])))
            

class Node:
    def __init__(self, data):
        self.data = data
        self.children = {}
        
    def insert_child(self, k, n):
        
        
        

def check(l, prev, cur, nl):
    nex = False
    if type(cur) == str:
        return(cur, nex)
    for dup in l[cur]:
        if dup[0] == prev:
            if dup[1] == nl:
                nex = dup[1]
            elif type(dup[1]) == str:
                nex = dup[1]
            else:
                pass
    return(cur, nex)
    
for key in r_dict:
    for i in range(len(r_dict[key])):
        for j in range(len(r_dict[key][i])):
            if j == 0 and not ord_list[ord(r_dict[key][i][j])]:
                ord_list[ord(r_dict[key][i][j])] = Node(r_dict[key][i][j])
            elif ord_list[ord(r_dict[key][i][j-1])]:
                ord_list[ord(r_dict[key][i][j-1])].insert_child(Node(r_dict[key][i][j], r = key))
                
if __name__ == "__main__":
    n = int(stdin.readline())
    for _ in range(n):
        line = stdin.readline().rstrip()
        i = 0
        new_line = ""
        while(i < len(line)):
            string = ""
            string += line[i]
            best = string
            j = 1
            for dup in ord_list[ord(line[i])]:
                if dup[0] == -1:
                    prev = -1
                    cur = ord(line[i])
                    j = 1
                    while(cur != False and i + j < len(line)):
                        print(prev,cur, j)
                        prev, cur = check(ord_list, prev, cur, ord(line[i + j]))
                        j += 1
                    if type(prev) == str:
                        string = prev
                        i += j - 1
                        break
                    j = 1
            i += j
            new_line += string
        stdout.write(new_line)
        stdout.write("\n")
            
                    
                        
                    
                    
                