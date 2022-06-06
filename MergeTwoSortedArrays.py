from os import *
from sys import *
from collections import *
from math import *

def ninjaAndSortedArrays(arr1,arr2,m,n):
    # Write your code here.
    for i in range(n):
        arr1[i+m]=arr2[i]
    arr1.sort()
    return arr1
