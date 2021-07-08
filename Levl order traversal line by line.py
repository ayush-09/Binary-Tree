# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 19:54:31 2021

@author: Ayush
"""

from collections import deque as queue

# One Queue

class Node():
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

def levelOrder(root):
    if root == None:
        return
    
    q= queue()
    
    q.append(root)
    q.append(None)
    
    while len(q)>1:
        c = q.popleft()
        
        if c==None:
            q.append(None)
            print()
        else:
            if c.left:
                q.append(c.left)
            if c.right:
                q.append(c.right)
            print(c.data, end=" ")
            
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    root.right.right.left = Node(7)
    root.right.right.right = Node(8)
    levelOrder(root)
    