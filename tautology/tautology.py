"""
file: tautology.py
author: @jalbers
"""

from sys import stdin,stdout
from collections import deque

class TautologyCheck:

    def __init__(self, logic_string):
        self.ls = logic_string
        self.w = None
        self.x = None
        self.stack = deque()
        self.p, self.q, self.r, self.s, self.t = [None] * 5
        self.fun_list = []
        self.is_tautology = True

    def check_logic(self, i = 0, bit_string = [0]*5):
        if i == 5:
            self.p, self.q, self.r, self.s, self.t = bit_string
            for f in self.fun_list:
                f()
            if not self.stack.pop():
                self.is_tautology = False
            return
        else:
            bit_string[i] = 1
            self.check_logic(i+1, bit_string)
            bit_string[i] = 0
            self.check_logic(i+1, bit_string)

    def push_p(self):
        self.stack.append(self.p)

    def push_q(self):
        self.stack.append(self.q)

    def push_r(self):
        self.stack.append(self.r)

    def push_s(self):
        self.stack.append(self.s)

    def push_t(self):
        self.stack.append(self.t)
    
    def f_N(self):
        arg1 = self.stack.pop()
        self.stack.append(not arg1)

    def f_K(self):
        arg1 = self.stack.pop()
        arg2 = self.stack.pop()
        self.stack.append(arg1 & arg2)

    def f_A(self):
        arg1 = self.stack.pop()
        arg2 = self.stack.pop()
        self.stack.append(arg1 | arg2)

    def f_C(self):
        arg1 = self.stack.pop()
        arg2 = self.stack.pop()
        if arg1 and not arg2:
            self.stack.append(False)
        else:
            self.stack.append(True)

    def f_E(self):
        arg1 = self.stack.pop()
        arg2 = self.stack.pop()
        self.stack.append(not(arg1 ^ arg2))

    def build_fun_list(self):
        self.fun_list = []
        for c in self.ls[::-1]:
            for i,j in zip(["K", "A", "N", "C", "E", "p", "q", "r", "s", "t"], \
                [self.f_K, self.f_A, self.f_N, self.f_C, self.f_E, self.push_p, self.push_q, self.push_r, self.push_s, self.push_t]):
                if c == i:
                    self.fun_list.append(j)

def main():
    for line in stdin:
        line = line.rstrip()
        if line == "0":
            return
        t = TautologyCheck(line)
        t.build_fun_list()
        t.check_logic()
        if t.is_tautology:
            stdout.write("tautology\n")
        else:
            stdout.write("not\n")

if __name__ == "__main__":
    main()