# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 16:52:25 2021

@author: Ayush
"""

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def diagonal(root):
    result=[]
    node = root
    leftq = deque()
    while node:
        result.append(node.data)
        if node.left:
            leftq.appendleft(node.left)
        if node.right:
            node=node.right
        else:
            if len(leftq)>=1:
                node = leftq.pop()
            else:
                node = None
    return result
    


# Driver Code
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.right.right.left = Node(13)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
 
print(diagonal(root))