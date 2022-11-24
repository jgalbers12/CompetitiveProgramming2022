"""
file: collatz_conjecture.py
author: @jalbers
"""

from sys import stdin,stdout

class Collatz:
    def __init__(self, a, b):
        self.init_a = a
        self.init_b = b
        self.a = a
        self.b = b
        self.a_dict = {self.a: 0}
        self.b_dict = {self.b: 0}
        self.a_count = 0
        self.b_count = 0
        self.first = 0

    def find_next(self, x):
        if x % 2 == 0:
            return(x//2)
        else:
            return(3*x + 1)
    
    def fill_next_a(self):
        self.a_count += 1
        val = self.find_next(self.a)
        if val not in self.a_dict.keys():
            self.a_dict[val] = self.a_count
            self.a = val
            return True
        else:
            return False

    def fill_next_b(self):
        self.b_count += 1
        val = self.find_next(self.b)
        if val not in self.b_dict.keys():
            self.b_dict[val] = self.b_count
            self.b = val
    
    # def fill_dict(self):
    #     while(self.a not in self.a_dict.keys()):
    #         self.fill_next()
        
    def find_answer(self):
        count = 0
        while(self.fill_next_a()):
            pass
        while(True):
            if self.b in self.a_dict.keys():
                self.first = self.b
                self.a_count = self.a_dict[self.first]
                self.b_count = count
                break
            else:
                count += 1
                self.b = self.find_next(self.b)

            # try: 
            #     first = self.a_dict[self.b]
            # except:
            #     self.b = self.find_next(self.b)
            #     count += 1
            # else:
            #     self.b_count = count
            #     self.first = self.b
            #     break
        # count = 0
        # while(val != self.b):
        #     #count += 1
        #     val = self.a_dict[val]
        # self.a_count = count

while True:
    line = stdin.readline().split()
    a = int(line[0])
    b = int(line[1])
    if a != 0:
        c = Collatz(a,b)
        c.find_answer()
        stdout.write(f"{c.init_a} needs {c.a_count} steps, {c.init_b} needs {c.b_count} steps, they meet at {c.first}\n")
    else:
        break