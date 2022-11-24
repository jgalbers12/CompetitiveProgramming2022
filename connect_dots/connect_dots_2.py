# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 13:30:38 2022

@author: jgalb
"""

from sys import stdin, stdout

class ConnectDots:
    def __init__(self, s):
        self.s = s
        self.rows = len(s)
        self.cols = len(s[0])
        self.nums = [chr(i) for i in range(ord("0"),ord("9")+1)] + [chr(i) for i in range(ord('a'),ord('z')+1)] + [chr(i) for i in range(ord("A"),ord("Z")+1)]
        self.max_index = len(self.nums) - 1
        self.non_nums = [".", "-", "|", "+"]
        
    def connect(self, a1, b1, a2, b2):
        if a1 == a2:
            if b1 < b2:
                dot1, dot2 = b1, b2
            else:
                dot1, dot2 = b2, b1
            for i in range(dot1+1, dot2):
                if self.s[a1][i] == "|":
                    self.s[a1][i] = "+"
                elif self.s[a1][i] == ".":
                    self.s[a1][i] = "-"
        else:
            if a1 < a2:
                dot1, dot2 = a1, a2
            else:
                dot1, dot2 = a2, a1
            for j in range(dot1+1, dot2):
                if self.s[j][b1] == ".":
                    self.s[j][b1] = "|"
                elif self.s[j][b1] == "-":
                    self.s[j][b1] = "+"
        
    def find_con(self, a, b, index):
        for i in range(0, self.rows):
            if (self.s[i][b] not in self.non_nums) and (index != self.max_index):
                if (self.s[i][b] == self.nums[index + 1]):
                    self.connect(a, b, i, b)
                    self.find_con(i, b, index + 1)
                    return
        for j in range(0, self.cols):
            if (self.s[a][j] not in self.non_nums) and (index != self.max_index):
                if (self.s[a][j] == self.nums[index + 1]):
                    self.connect(a, b, a, j)
                    self.find_con(a, j, index + 1)
                    return
        return
    def scan(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.s[i][j] not in self.non_nums:
                    if self.s[i][j] == "0":
                        self.find_con(i, j, 0)
                    
if __name__ == "__main__":
    grid = []
    ans_list = []
    for line in stdin:
        if line == '\r\n':
            prob = ConnectDots(grid)
            prob.scan()
            for line in prob.s:
                ans_list.append("".join(line) + "\r\n")
                # stdout.write("".join(line) + "\r\n")
            grid = []
            ans_list.append("\r\n")
        else:
            grid.append([*line.rstrip()])
    for i in range(len(ans_list)-2):
        stdout.write(ans_list[i])
    stdout.write(ans_list[-2][0:-2])
    # else:
    #     prob = ConnectDots(grid)
    #     prob.scan()
    #     for line in prob.s:
    #         stdout.write("".join(line) + "\r\n")