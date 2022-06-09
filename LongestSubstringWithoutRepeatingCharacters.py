from os import *
from sys import *
from collections import *
from math import *

def uniqueSubstrings(input ) :
    charSet=set()
    res=0
    l=0
    for r in range(len(input)):
        while input[r] in charSet:
            charSet.remove(input[l])
            l+=1
        charSet.add(input[r])
        res=max(res,r-l+1)
    return res
