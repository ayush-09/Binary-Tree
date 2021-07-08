# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 21:09:50 2021

@author: Ayush
"""
 # Morris O(1)
class Node:
    def __init__(self,data, left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
        
def morris_traversal(root):
    curr = root
    while curr is not None:
        if curr.left is None:
            yield curr.data
            curr = curr.right
        else:
            pre = curr.left
            while pre.right is not None and pre.right is not curr:
                pre = pre.right
            if pre.right == None:
                pre.right = curr
                curr = curr.left
            else:
                pre.right = None
                yield curr.data
                curr = curr.right

if __name__=="__main__":
    root = Node(1,right=Node(3),left=Node(2, left=Node(4),right=Node(5)))
    for i in morris_traversal(root):
        print(i,end=" ")


# Iterative
        
class INode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(root):
    s=[]
    curr = root
    while True:
        if curr is not None:
            s.append(curr)
            curr = curr.left
        elif s:
            curr = s.pop()
            print(curr.data,end=" ")
            curr = curr.right
        else:
            break
    print()
        
if __name__ =="__main__":
    root=INode(1)
    root.left = INode(2)
    root.right=INode(3)
    root.left.left = INode(4)
    root.left.right = INode(5)
    
    inOrder(root)

