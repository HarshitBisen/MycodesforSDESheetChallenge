from os import *
from sys import *
from collections import *
from math import *

def majorityElementII(arr):
    n=len(arr)
    target=n//3
    dict={}
    ls=[]
    for i in arr:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    for key,item in dict.items():
        if item>target:
            ls.append(key)
    return ls
