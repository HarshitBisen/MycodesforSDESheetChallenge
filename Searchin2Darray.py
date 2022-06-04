from os import *
from sys import *
from collections import *
from math import *

def findTargetInMatrix(mat, m, n, target):
    rows=len(mat)
    cols=len(mat[0])
    top,bottom=0,m-1
    row=0
    while top<=bottom:
        row=(top+bottom)//2
        if target>mat[row][cols-1]:
            top=row+1
        elif target<mat[row][0]:
            bottom=row-1
        else:
            break
    if top>bottom:
        return False
    
    l,r=0,n-1
    while l<=r:
        mid=(l+r)//2
        if target<mat[row][mid]:
            r=mid-1
        elif target>mat[row][mid]:
            l=mid+1
        else:
            return True
    return False
