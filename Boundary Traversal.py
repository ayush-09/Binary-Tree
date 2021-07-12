# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 18:49:55 2021

@author: Ayush
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
def printLeafs(root):
    if root:
        printLeafs(root.left)
        if root.left is None and root.right is None:
            print(root.data)
        printLeafs(root.right)
        
def printBoundaryLeft(root):
    if root:
        if root.left:
            print(root.data)
            printBoundaryLeft(root.left)
        elif root.right:
            print(root.data)
            printBoundaryLeft(root.right)

def printBoundaryRight(root):
     
    if(root):
        if (root.right):
            printBoundaryRight(root.right)
            print(root.data)
         
        elif(root.left):
            printBoundaryRight(root.left)
            print(root.data)

def printBoundary(root):
    if (root):
        print(root.data)
         
        printBoundaryLeft(root.left)
 
        printLeafs(root.left)
        printLeafs(root.right)
 
        printBoundaryRight(root.right)
 
 
# Driver program to test above function
root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)
printBoundary(root)