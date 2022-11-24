# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:44:12 2022

@author: jgalb
"""

from sys import stdin

class match:
    def __init__(self,n):
        self.n = n
        self.flipped={}
        self.flipped_matches = []
        
    def flip_cards(self, pos1, pos2, name1, name2):
        for (pos, name) in zip([pos1,pos2],[name1,name2]):
            if name not in self.flipped.keys():
                self.flipped[name] = [pos]
            elif pos not in self.flipped[name]:
                self.flipped[name].append(pos)
        if name1 == name2:
            self.flipped_matches.append(name1)
            self.flipped.pop(name1)
            
    def find_remaining(self):
        num_matches = 0
        one_flipped = 0
        two_flipped = 0
        for key in self.flipped:
            if len(self.flipped[key]) == 1:
                one_flipped += 1
            else:
                two_flipped += 1
        total_known = 2*(len(self.flipped_matches) + two_flipped) + one_flipped
        if n - (total_known) == one_flipped:
            num_matches = two_flipped + one_flipped
        elif n - total_known == 2:
            num_matches = two_flipped + 1
        else:
            num_matches = two_flipped        
        print(num_matches)

if __name__ == "__main__":
    n = int(stdin.readline())
    k = int(stdin.readline())
    m = match(n)
    for i in range(k):
        line = stdin.readline().split()
        p1 = int(line[0])
        p2 = int(line[1])
        c1 = line[2]
        c2 = line[3]
        m.flip_cards(p1,p2,c1,c2)
    m.find_remaining()