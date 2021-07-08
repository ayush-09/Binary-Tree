# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 20:08:13 2021

@author: Ayush
"""

# Use fn to print current level O(n^2)

class Node():
    def __init__(self,key):
        self.data = key
        self.left= None
        self.right = None

def printLevelOrder(root):
    h = height(root)
    for i in range(1,h+1):
        printCurrentLevel(root,i)
        
def printCurrentLevel(root,level):
    if root ==None:
        return 
    if level==1:
        print(root.data,end=" ")
    elif level>1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)
        
def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
    if lheight > rheight :
        return lheight+1
    else:
        return rheight+1
    
root = Node(1)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(3)
root.left.right = Node(6)

print("Level order traversal of binary tree is -")
printLevelOrder(root)


# using queue O(n)

class Node():
    def __init__(self,key):
        self.data = key
        self.left= None
        self.right = None
        
        
def printLevelOrder(root):
    if root is None:
        return
    queue=[]
    queue.append(root)
    
    while(len(queue) > 0):
        print (queue[0].data)
        node = queue.pop(0)
 
        if node.left is not None:
            queue.append(node.left)
 
        if node.right is not None:
            queue.append(node.right)
    
root = Node(1)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(3)
root.left.right = Node(6)

print("Level order traversal of binary tree is -")
printLevelOrder(root)