from os import *
from sys import *
from collections import *
from math import *

def maximumProfit(prices):
    # Write your code here.
    n = len(prices)
    l,r=0,1
    maxprofit=0
    
    while r<n:
        prof=0
        if prices[r]>prices[l]:
            prof=prices[r]-prices[l]
            maxprofit=maxprofit if maxprofit>prof else prof
        else:
            l=r
        r+=1
    return maxprofit
