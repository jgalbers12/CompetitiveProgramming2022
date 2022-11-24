# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 19:58:05 2022

@author: jgalb
"""

from sys import stdin, stdout

r_dict = {"@":["at", "At"], "&":["and", "And"], "1":["one", "One","won", "Won"], "2":["to", "To","too", "Too","two", "Two"], "4":["for", "four", "For", "Four"], \
          "b":["bea","be","bee"], "B":["Bea","Be","Bee"],"c":["sea","see"], "C":["Sea","See"], "i":["eye"], "I":["Eye"], "o":["oh","owe"],"O":["Oh","Owe"], \
              "r":["are"], "R":["Are"],"u":["you"], "U":["You"], "y":["why"], "Y":["Why"]}

class Node:
    def __init__(self):
        self.children = [None]*75
        self.is_end = False
        self.key = None
        
class Tree:
    def __init__(self):
        self.root = Node()
        
    def make_node(self):
        return(Node())
    
    def char_to_index(self, c):
        return(ord(c) - ord("0"))
    
    def add_to_tree(self, word, key):
        cur_node = self.root
        for i in range(len(word)):
            index = self.char_to_index(word[i])
            if not cur_node.children[index]:
                cur_node.children[index] = self.make_node()
            cur_node = cur_node.children[index]
        cur_node.is_end = True
        cur_node.key = key
        
        
def char_to_index(c):
     return(ord(c) - ord("0"))

tree_list = [None] * 75

for key in r_dict:
    for word in r_dict[key]:
        first_i = char_to_index(word[0])
        if not tree_list[first_i]:
            tree_list[first_i] = Tree()
        tree_list[first_i].add_to_tree(word[1:], key)
        
def search_tree(tree, string, index):
    j = 1
    cur_node = tree.root
    cur_char = char_to_index(string[index + j])
    while(cur_node.children[cur_char]):
        j += 1
        cur_node = cur_node.children[cur_char]
        if index + j < len(string):
            cur_char = char_to_index(string[index + j])
    if(cur_node.key):
        return(j, cur_node.key)
    else:
        return(1, string[index])
    
def index_to_char(i):
    return(chr(i + ord("0")))

n = int(stdin.readline())
for i in range(n):
    string = stdin.readline().rstrip()
    index = 0
    new_string = ""
    while(index < len(string)):
        cur_char = char_to_index(string[index])
        tree = tree_list[cur_char]
        if tree and index < len(string) - 1:
            j, key = search_tree(tree, string, index)
            index += j
            new_string += key
        else:
            new_string += string[index]
            index += 1
    stdout.write(new_string)
    if i < n-1:
        stdout.write("\n")
            
    

        