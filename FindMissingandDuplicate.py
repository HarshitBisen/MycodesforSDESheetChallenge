from os import *
from sys import *
from collections import *
from math import *

def missingAndRepeating(arr, n):
    # Write your code here
    miss,repeat=0,0
    sumn=(n*(n+1))//2
    sumn2=(n*(n+1)*(2*n+1))//6
    suma,suma2=0,0
    for i in arr:
        suma+=i
        suma2+=i*i
    A=sumn-suma
    B=sumn2-suma2
    C=B//A
    miss=(C+A)//2
    repeat=(C-A)//2
    return (miss,repeat)
