from os import *
from sys import *
from collections import *
from math import *

def pairSum(arr, s):
    n=len(arr)
    ans=[]
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==s:
                temp=[]
                temp.append(min(arr[i],arr[j]))
                temp.append(max(arr[i],arr[j]))
                ans.append(temp)
    ans.sort()
    return ans
                
