from os import *
from sys import *
from collections import *
from math import *

import sys
sys.setrecursionlimit(10**7)

def modularExponentiation(x, n, m):
    if n==0:
        return 1
    elif n%2==0:
        y=modularExponentiation(x,n/2,m)
        return (y*y)%m
    else:
        return ((x%m)*modularExponentiation(x,n-1,m))%m
        
        

# Main.
t = int(input())
while (t > 0):
	lst = list(map(int,input().split()))
	x,n,m = lst[0], lst[1], lst[2]
	print(modularExponentiation(x, n, m))
	t -= 1
