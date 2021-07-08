# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 19:44:43 2021

@author: Ayush
"""

class Node:
    def __init__(self,data):
        self.data =data
        self.left = None
        self.right = None
        
def newNode(val):
    temp = Node(0)
    temp.data = val
    temp.left = None
    temp.right = None
    
    return temp
    
def inorderSuccessor(root,target_node):
    global next
    
    if root==None:
        return
    inorderSuccessor(root.right, target_node)
    
    if root.data == target_node.data:
        if next== None:
            print("Inorder successor of",root.data ,"is:None")
        else:
            print("inorder successor of",root.data,"is:",next.data)
    next=root
    inorderSuccessor(root.left, target_node)
    
next=None

if __name__ == '__main__': 
      
    # Let's construct the binary tree 
    # as shown in above diagram.
    root = newNode(1) 
    root.left = newNode(2) 
    root.right = newNode(3) 
    root.left.left = newNode(4) 
    root.left.right = newNode(5) 
    root.right.right = newNode(6) 
      
    # Case 1 
    next = None
    inorderSuccessor(root, root.right) 
  
    # case 2 
    next = None
    inorderSuccessor(root, root.left.left) 
  
    # case 3 
    next = None
    inorderSuccessor(root, root.right.right)