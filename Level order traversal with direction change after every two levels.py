# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 20:35:52 2021

@author: Ayush
"""

from collections import deque

# Iterative
class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None


def modifiedLevelOrder(node):
    
    if node == None:
        return
    if node.left == None and node.right==None:
        print(node.data, end=" ")
        return
    myQueue = deque()
    myStack=[]
    temp = None
    sz=0
    ct = 0
    rightToLeft = False
    
    myQueue.append(node)
    
    while (len(myQueue)>0):
        ct+=1
        sz= len(myQueue)
        
        for i in range(sz):
            temp = myQueue.popleft()
            
            if rightToLeft==False:
                print(temp.data,end=" ")
            else:
                myStack.append(temp)
                
            if temp.left:
                myQueue.append(temp.left)
            if temp.right:
                myQueue.append(temp.right)
                
        if rightToLeft==True:
            while(len(myStack)>0):
                temp = myStack[-1]
                myStack.pop()
                print(temp.data,end=" ")
        if ct==2:
            rightToLeft = not rightToLeft
            ct=0
        print()
        
if __name__ == '__main__':
   
    # Let us create binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(3)
    root.left.right.right = Node(1)
    root.right.left.left = Node(4)
    root.right.left.right = Node(2)
    root.right.right.left = Node(7)
    root.right.right.right = Node(2)
    root.left.right.left.left = Node(16)
    root.left.right.left.right = Node(17)
    root.right.left.right.left = Node(18)
    root.right.right.left.right = Node(19)
 
    modifiedLevelOrder(root)             
    
#Recursive

class NNode:
    def __init__(self,data):
        self.data = data
        self.left= None
        self.right = None
def height(root):
    if root==None:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)
        
        if lheight > rheight:
            return 1+ lheight
        else:
            return 1+ rheight
        
def printLevel(root,level,stack=False):
    global ss
    if root == None:
        return
    if level==1 and stack==True:
        ss.append(root.data)
    elif level==1 and stack==False:
        print(root.data,end=" ")
    elif level>1:
        printLevel(root.left, level-1,stack=stack)
        printLevel(root.right, level-1,stack=stack)
        
def print_2_Levels(root):
    if root==None:
        return
    h = height(root)
    c=0
    for i in range(1,h+1):
        global ss
        ss=[]
        
        if c<2:
            printLevel(root, i,stack=False)
        else:
            printLevel(root, i,stack=True)
            
            for i in range(len(ss)-1,-1,-1):
                print(ss[i],end=" ")
            if c==3:
                c=-1
        c +=1
        print("")
        
if __name__ == "__main__":
    root = NNode(1)
    root.left      = NNode(2)
    root.right     = NNode(3)
    root.left.left  = NNode(4)
    root.left.right  = NNode(5)
    root.right.left = NNode(6)
    root.right.right = NNode(7)
    root.left.left.left = NNode(8)
    root.left.left.right = NNode(9)
    root.left.right.left = NNode(3)
    root.left.right.right = NNode(1)
    root.right.left.left = NNode(4)
    root.right.left.right = NNode(2)
    root.right.right.left = NNode(7)
    root.right.right.right = NNode(2)
    root.left.left.right.left = NNode(16)
    root.left.right.right.left = NNode(17)
    root.left.right.right.right = NNode(18)
    root.right.left.right.right = NNode(19)
    print("Different levels:")
     
    # Function Call
    print_2_Levels(root)

