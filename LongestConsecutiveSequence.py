from os import *
from sys import *
from collections import *
from math import *

def lengthOfLongestConsecutiveSequence(arr, n):
    num=set(arr)
    c=0
    for n in arr:
        if (n-1) not in num:
            length=0
            while n+length in num:
                length+=1
            c=max(c,length)
    
    return c
