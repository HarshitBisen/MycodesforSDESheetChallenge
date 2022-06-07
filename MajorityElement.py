from os import *
from sys import *
from collections import *
from math import *

def findMajorityElement(arr, n):
    target = n//2
    dict={}
    for i in arr:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    for key,item in dict.items():
        if item>target:
            return key
    return -1
