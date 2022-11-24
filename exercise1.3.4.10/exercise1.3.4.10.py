# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 12:59:23 2022

@author: jgalb
"""

import re

class Replacer:
    def __init__(self, string):
        self.string = string
        
    def replace(self):
        self.string = re.sub(r"\b[a-z][0-9]{2}\b", "***", self.string)
        
    def print_string(self):
        print(self.string)
        

s = "a72 a73 aa73 aaa dddd d83"

rep = Replacer(s)
rep.replace()
rep.print_string()