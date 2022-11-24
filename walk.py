# Skeleton file for 'treeWalk.py'

class Node:
    def __init__(self, key, left, right, p):
        self.key = key
        self.left = left
        self.right = right
        self.p = p

def preorder(x):
    if (x != None):
        print(x.key)
        preorder(x.left)
        preorder(x.right)

def inorder(x):
    if (x != None):
        inorder(x.left)
        print(x.key)
        inorder(x.right)

def postorder(x):
    if (x != None):
        postorder(x.left)
        postorder(x.right)
        print(x.key)

########################## begin ####################
def iter_preorder(x):
    print(x.key)
    last = None
    root = x
    if x.left:
        last = x
        x = x.left
    elif x.right:
        last = x
        x = x.right
    else:
        return
    while(True):
        if last == x.left:
            if x.right:
                last = x
                x = x.right
            elif x != root:
                last = x
                x = x.p
            else:
                break
        elif last == x.right:
            if x != root:
                last = x
                x = x.p
            else:
                break
        elif last == x.p:
            print(x.key)
            if x.left:
                last = x
                x = x.left
            elif x.right:
                last = x
                x = x.right
            else:
                last = x
                x = x.p

def iter_inorder(x):
    last = None
    root = x
    if x.left:
        last = x
        x = x.left
    elif x.right:
        last = x
        x = x.right
    else:
        print(x.key)
        return
    while(True):
        if last == x.left:
            print(x.key)
            if x.right:
                last = x
                x = x.right
            elif x != root:
                last = x
                x = x.p
            else:
                break
        elif last == x.right:
            if x != root:
                last = x
                x = x.p
            else:
                break
        elif last == x.p:
            if x.left:
                last = x
                x = x.left
            elif x.right:
                last = x
                x = x.right
            else:
                print(x.key)
                last = x
                x = x.p

def iter_postorder(x):
    last = None
    root = x
    if x.left:
        last = x
        x = x.left
    elif x.right:
        last = x
        x = x.right
    else:
        print(root.key)
        return
    while(True):
        if last == x.left:
            if x.right:
                last = x
                x = x.right
            elif x != root:
                print(x.key)
                last = x
                x = x.p
            else:
                print(x.key)
                break
        elif last == x.right:
            if x.p and x != root:
                print(x.key)
                last = x
                x = x.p
            else:
                print(x.key)
                break
        elif last == x.p:
            if x.left:
                last = x
                x = x.left
            elif x.right:
                last = x
                x = x.right
            else:
                print(x.key)
                last = x
                x = x.p

########################## end ####################

########################## testing ####################
def main():
    x1 = Node(1, None, None, None)
    x2 = Node(2, None, None, None)
    x3 = Node(3, None, None, None)
    x4 = Node(4, None, None, None)
    x5 = Node(5, None, None, None)
    x6 = Node(6, None, None, None)

    x1.p = x2
    x2.left = x1; x2.right = x3; x2.p = x4
    x3.p = x2
    x4.left = x2;  x4.right = x6
    x5.p = x6
    x6.left = x5; x6.p = x4

    for x in [x1, x2, x3, x4, x5, x6]:
        print("recursive preorder:")
        preorder(x)
        print("")
        print("iterative preorder:")
        iter_preorder(x)
        print("")
        print("recursive inorder:")
        inorder(x)
        print("")
        print("iterative inorder:")
        iter_inorder(x)
        print("")
        print("recursive postorder:")
        postorder(x)
        print("")
        print("iterative postorder:")
        iter_postorder(x)
        print("")

if __name__ == '__main__':
    main()