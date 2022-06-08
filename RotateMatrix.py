from os import *
from sys import *
from collections import *
from math import *


def rotateMatrix(mat, n, m):
    row,col=0,0
    lastrow,lastcol=n,m
    prev,cur=0,0
    
    while row<lastrow and col<lastcol:
        if row+1==lastrow or col+1==lastcol:
            return mat
        prev=mat[row+1][col]
        for i in range(col,lastcol):
            cur=mat[row][i]
            mat[row][i]=prev
            prev=cur
        row+=1
        for i in range(row,lastrow):
            cur=mat[i][lastcol-1]
            mat[i][lastcol-1]=prev
            prev=cur
        lastcol-=1
        if row<lastrow:
            for i in range(lastcol-1,col-1,-1):
                cur=mat[lastrow-1][i]
                mat[lastrow-1][i]=prev
                prev=cur
        lastrow-=1
        if col<lastcol:
            for i in range(lastrow-1,row-1,-1):
                cur=mat[i][col]
                mat[i][col]=prev
                prev=cur
        col+=1
        
            
