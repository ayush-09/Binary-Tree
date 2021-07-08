# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 09:30:08 2021

@author: Ayush
"""
# Naive Method (Recursion)
def search(arr, x, n):
    for i in range(n):
        if arr[i]==x:
            return i
    return -1

def printPostOrder(In,pre,n):
    root=search(In, pre[0], n)
    if root!=0:
        printPostOrder(In, pre[1:n], root)
        
    if root !=n - 1:
        printPostOrder(In[root+1:n], pre[root+1:n], n-root-1)
        
    print(pre[0],end=" ")
    

if __name__=="__main__":
    In = [ 4, 2, 5, 1, 3, 6 ]
    pre = [ 1, 2, 4, 5, 3, 6 ]
    n = len(In)
     
    print("Postorder traversal ")
     
    printPostOrder(In, pre, n)
