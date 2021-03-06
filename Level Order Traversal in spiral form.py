# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 19:06:26 2021

@author: Ayush
"""
# Recursive O(n^2)

class Node():
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key
        
def printSpiral(root):
    h = height(root)
    ltr = False
    for i in range(1,h+1):
        printGivenLevel(root,i,ltr)
        ltr = not ltr
def printGivenLevel(root,level,ltr):
    if root == None:
        return
    if level==1:
        print(root.data,end=" ")
    elif level>1:
        if ltr:
            printGivenLevel(root.left, level-1, ltr)
            printGivenLevel(root.right, level-1, ltr)
        else:
            printGivenLevel(root.right, level-1, ltr)
            printGivenLevel(root.left, level-1, ltr)

def height(node):
    if node == None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
        
        if (lheight>rheight):
            return lheight+1
        else:
            return rheight+1
        
if __name__=="__main__":
    av= Node(3)
    av.left = Node(1)
    av.right = Node(2)
    av.left.left = Node(7) 
    av.left.right = Node(6) 
    av.right.left = Node(5) 
    av.right.right = Node(4) 
    print("Spiral Order traversal of binary tree is") 
    printSpiral(av) 
      
    
#Iterative

class newNode():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printSpiral2(root):
    if root==None:
        return
    s1=[]
    s2=[]
    s1.append(root)
    
    while not len(s1)==0 or not len(s2)==0:
        while not len(s1)==0:
            temp=s1[-1]
            s1.pop()
            print(temp.data, end=" ")
            
            if temp.left:
                s2.append(temp.left)
            else:
                s2.append(temp.right)
        while not len(s2)==0:
            temp=s2[-1]
            s2.pop()
            print(temp.data, end=" ")
            
            if temp.left:
                s1.append(temp.left)
            else:
                s1.append(temp.right)


if __name__ == '__main__':
    root = newNode(1) 
    root.left = newNode(2) 
    root.right = newNode(3) 
    root.left.left = newNode(7) 
    root.left.right = newNode(6) 
    root.right.left = newNode(5) 
    root.right.right = newNode(4) 
    print("Spiral Order traversal of",
                    "binary tree is ") 
    printSpiral(root)
    
    
    
    
    
    












    