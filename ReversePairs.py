from os import *
from sys import *
from collections import *
from math import *

def reversePairs(arr, n):
    return mergesort(arr,0,n-1)

def mergesort(arr,low,high):
    if low>=high:
        return 0
    mid=(low+high)//2
    inv=mergesort(arr,low,mid)
    inv+=mergesort(arr,mid+1,high)
    inv+=merge(arr,low,mid,high)
    return inv

def merge(arr,low,mid,high):
    count=0
    j=mid+1
    for i in range(low,mid+1):
        while j<=high and arr[i]>2*arr[j]:
            j+=1
        count+=j-(mid+1)
    temp=[]
    left,right=low,mid+1
    while left<=mid and right<=high:
        if arr[left]>arr[right]:
            temp.append(arr[right])
            right+=1
        else:
            temp.append(arr[left])
            left+=1
    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right<=high:
        temp.append(arr[right])
        right+=1
    for i in range(low,high+1):
        arr[i]=temp[i-low]
    return count
