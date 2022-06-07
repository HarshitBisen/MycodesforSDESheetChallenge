from os import *
from sys import *
from collections import *
from math import *

def LongestSubsetWithZeroSum(arr):
    sum=0
    maxi=0
    dict={}
    n=len(arr)
    for i in range(n):
        sum+=arr[i]
        if sum==0:
            maxi=i+1
        else:
            if sum in dict:
                maxi=max(maxi,i-dict[sum])
            else:
                dict[sum]=i
    return maxi
