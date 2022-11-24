"""
file: arithmetic.py
author: @jalbers
"""

from sys import stdin, stdout

num = stdin.readline()
num = int(num, 8)
stdout.write(str(hex(num)).upper()[2:])