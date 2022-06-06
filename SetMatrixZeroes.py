from os import *
from sys import *
from collections import *
from math import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
    rows,cols=len(matrix),len(matrix[0])
    rowzero=False
    
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c]==0:
                matrix[0][c]=0
                if r>0:
                    matrix[r][0]=0
                else:
                    rowzero=True
    for r in range(1,rows):
        for c in range(1,cols):
            if matrix[r][0]==0 or matrix[0][c]==0:
                matrix[r][c]=0
    if matrix[0][0]==0:
        for r in range(rows):
            matrix[r][0]=0
    if rowzero==True:
        for c in range(cols):
            matrix[0][c]=0
                    
