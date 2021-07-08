# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 20:44:32 2021

@author: Ayush
"""

#Recursion
class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def reverseLevelOrder(root):
    h = height(root)
    for i in reversed(range(1,h+1)):
        printGivenLevel(root,i)
        
def printGivenLevel(root,level):
    if root ==None:
        return
    if level == 1:
        print(root.data,end=" ")
        
    elif level>1:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level-1)

def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
        
        if lheight > rheight:
            return lheight +1
        else:
            return rheight +1
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
  
print("Level Order traversal of binary tree is")
reverseLevelOrder(root)


  
from collections import deque
# A binary tree node
class Node:
  
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
  
def reverseLevelOrder(root):

    q = deque()
    q.append(root)
    ans = deque()
    while q:
        node = q.popleft()
        if node is None:
            continue
          
        ans.appendleft(node.data)
          
        if node.right:
            q.append(node.right)
              
        if node.left:
            q.append(node.left)
              
    return ans
  
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
  
print("Level Order traversal of binary tree is")
reverseLevelOrder(root)
  
