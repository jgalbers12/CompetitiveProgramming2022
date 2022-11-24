# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 12:45:40 2022

@author: jgalb
"""

from sys import stdin
import datetime

class birthday_choose:
    def __init__(self):
        self.days = [False] * 365
        self.best = 0
    
    def fill(self, d):
        first = datetime.date(2022,10,28)
        birthd = datetime.date.fromisoformat(d)
        diff = (birthd - first).days
        if diff < 0:
            diff += 365
        self.days[diff] = True
        
    def find_best(self):
        counter = 0
        first = 0
        hit_first = False
        max_c = 0
        best = 0
        for i in range(len(self.days)):
            if self.days[i]:
                if not hit_first:
                    first = i
                    hit_first = True
                if counter > max_c:
                    max_c = counter
                    best = i-1
                counter = 0
            else:
                counter += 1
        if (counter + first) > max_c:
            best = first - 1
        if (counter + first == max_c) & (first != 0) & (max_c != 0):
            best = first - 1
        self.best = best
    
    def print_best(self):
        delt = datetime.timedelta(days=self.best)
        best_date = datetime.date(2022,10,28) + delt
        print(best_date.isoformat()[5:])
        
if __name__ == "__main__":
    b = birthday_choose()
    n = int(stdin.readline())
    for i in range(n):
        bd_str = stdin.readline().split()[1]
        b.fill("2022-"+bd_str)
    b.find_best()
    b.print_best()