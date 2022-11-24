# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 21:47:14 2022

@author: jgalb
"""

from sys import stdin

if __name__ == "__main__":
    line = stdin.readline().split()
    goal = int(line[0])
    to_reg = int(line[1])
    to_office = int(line[2])
    min_steps = goal
    office_to_reg = abs(to_office - to_reg)
    add = 0
    if office_to_reg%2 != (goal-to_office)%2:
        add = 1
    if goal <= to_office + office_to_reg:
        min_steps = to_office + office_to_reg + to_reg
    else:
        min_steps = to_office + (goal - to_office) + to_reg + add
    print(min_steps)