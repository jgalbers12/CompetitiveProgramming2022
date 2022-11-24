# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 15:21:00 2022

@author: jgalb
"""

from sys import stdin

finger_dict = {"c":[2,3,4,7,8,9,10], "d":[2,3,4,7,8,9], "e":[2,3,4,7,8], \
               "f":[2,3,4,7], "g":[2,3,4], "a":[2,3], "b":[2], \
                   "C":[3], "D":[1,2,3,4,7,8,9], "E":[1,2,3,4,7,8], "F":[1,2,3,4,7], \
                       "G":[1,2,3,4], "A":[1,2,3], "B":[1,2], "n":[]}

n = int(stdin.readline())
for i in range(n):
    finger_count = [0] * 10
    note_string = stdin.readline().strip()
    last_note = "n"
    for c in note_string:
        for f in finger_dict[c]:
            if f not in finger_dict[last_note]:
                finger_count[f-1] += 1
        last_note = c
    print(" ".join([str(x) for x in finger_count]))
