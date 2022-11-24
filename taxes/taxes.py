# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 22:28:37 2022

@author: jgalb
"""

from sys import stdin

class Mittens:
    def __init__(self):
        self.shares = 0
        self.price = 0.0

    def buy(self, x, c):
        new_shares = self.shares + x
        self.price = (self.price*self.shares + x*c) / (new_shares)
        self.shares = new_shares
        
    def sell(self, x):
        self.shares -= x
    
    def split(self, x):
        self.shares = self.shares * x
        self.price = self.price / x
        
    def merge(self, x):
        self.shares = self.shares // x
        self.price = self.price * x
        
    def dies(self, y):
        if y > self.price:
            final = self.shares * (y - ((y - self.price) * .3))
        else:
            final = self.shares * y
        print(final)

if __name__ == "__main__":
    m = Mittens()
    while(True):
        i = stdin.readline().split()
        if i[0] == "buy":
            m.buy(int(i[1]), int(i[2]))
        elif i[0] == "sell":
            m.sell(int(i[1]))
        elif i[0] == "split":
            m.split(int(i[1]))
        elif i[0] == "merge":
            m.merge(int(i[1]))
        else:
            m.dies(int(i[1]))
            break
        