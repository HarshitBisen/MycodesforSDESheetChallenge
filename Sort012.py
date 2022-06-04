from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def sort012(arr, n) :

	# write your code here
    # don't return anything 
    c0,c1,c2 = 0,0,0
    for i in range(n):
        if arr[i]==0:
            c0+=1
        elif arr[i]==1:
            c1+=1
        else:
            c2+=1
    i=0
    while i<c0:
        arr[i]=0
        i+=1
    j=i
    while j<i+c1:
        arr[j]=1
        j+=1
    k=j
    while k<j+c2:
        arr[k]=2
        k+=1


#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n



def printAnswer(arr, n) :
    
    for i in range(n) :
        
        print(arr[i],end=" ")
        
    print()
    
#main

t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    sort012(arr, n)
    printAnswer(arr, n)
