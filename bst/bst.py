"""
file: bst.py
author: @jalbers
"""

class BST:
    def __init__(self, root_key):
        self.counter = 0
        self.root = Node(root_key, self.root)
        pass

    def search(self, x):
        pass

    def insert(self, x):
        pass


class Node:
    def __init__(self, key, p):
        self.key = key
        self.right = None
        self.left = None
        self.p = p