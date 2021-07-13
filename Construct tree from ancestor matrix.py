# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 20:51:05 2021

@author: Ayush
"""

class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data,end=" ")
        inorder(node.right)

def constructBT(mat):
    n = len(mat)
    dict = {}
    for i in range(n):
        total = sum(mat[i])
        dict.setdefault(total, []).append(i)
    node = [Node(-1)]*n
    last = 0
    
    parent = [False] * n
    
    for key in dict.keys():
        for r in dict.get(key):
            last=r
            node[r] = Node(r)
            if key==0:
                continue
            for i in range(n):
                if not parent[i] and mat[r][i]==1:
                    if node[r].left is None:
                        node[r].left = node[i]
                    else:
                        node[r].right = node[i]
                        
                    parent[i] = True
    return node[last]

if __name__ == '__main__':
 
    mat = [[0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0]]
 
    root = constructBT(mat)
    inorder(root)