# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 23:39:09 2022

@author: jgalb
"""

from sys import stdin

class tictactoe:
    def __init__(self, board):
        self.board = board
        self.x_r_threes = 0
        self.x_d_threes = 0
        self.x_c_threes = 0
        self.o_r_threes = 0
        self.o_d_threes = 0
        self.o_c_threes = 0
        self.nx = 0
        self.no = 0
        
    def count(self):
        for row in self.board:
            for j in row:
                if j == "X":
                    self.nx += 1
                elif j == "O":
                    self.no += 1
        
    def check_rows(self):
        for a in ["X", "O"]:
            for row in self.board:
                if row[0] == row[1] == row[2] == a:
                    if a == "X":
                        self.x_r_threes += 1
                    else:
                        self.o_r_threes += 1
                    
    def check_cols(self):
        for a in ["X", "O"]:
            for i in range(3):
                if self.board[0][i] == self.board[1][i] == self.board[2][i] == a:
                    if a == "X":
                        self.x_c_threes += 1
                    else:
                        self.o_c_threes += 1
                    
    def check_diags(self):
        for a in ["X", "O"]:
            if self.board[0][0] == self.board[1][1] == self.board[2][2] == a:
                if a == "X":
                    self.x_d_threes += 1
                else:
                    self.o_d_threes += 1
            if self.board[2][0] == self.board[1][1] == self.board[0][2] == a:
                if a == "X":
                    self.x_d_threes += 1
                else:
                    self.o_d_threes += 1
                
    def find_ans(self):
        self.count()
        self.check_rows()
        self.check_cols()
        self.check_diags()
        o_threes = self.o_c_threes + self.o_d_threes + self.o_r_threes
        x_threes = self.x_c_threes + self.x_d_threes + self.x_r_threes
        if (self.nx == self.no):       
            if (o_threes + x_threes) == 0:
                print("yes")
            elif (o_threes == 1) & (x_threes == 0):
                print("yes")
            else:
                print("no")
        elif (self.nx == self.no + 1):
            if (x_threes == 0) & (o_threes == 0):
                print("yes")
            elif (x_threes == 1) & (o_threes == 0):
                print("yes")
            elif self.x_r_threes == self.x_d_threes == 1:
                print("yes")
            elif self.x_c_threes == self.x_d_threes == 1:
                print("yes")
            elif self.x_d_threes == 2:
                print("yes")
            elif self.x_c_threes == self.x_r_threes == 1:
                print("yes")
            else:
                print("no")
        else:
            print("no")
            
if __name__ == "__main__":
    n = int(stdin.readline())
    for _ in range(n):
        l1 = stdin.readline()
        r1 = [l1[i] for i in range(3)]
        l2 = stdin.readline()
        r2 = [l2[i] for i in range(3)]
        l3 = stdin.readline()
        r3 = [l3[i] for i in range(3)]
        b = [r1, r2, r3]
        ttt = tictactoe(b)
        ttt.find_ans()
        stdin.readline()
            