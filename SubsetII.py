from typing import *

  
def uniqueSubsets(n :int,arr :List[int]) -> List[List[int]]:
    res=[]
    arr.sort()
    
    def backtrack(i,subset):
        if i==len(arr):
            res.append(subset[::])
            return  
        
        subset.append(arr[i])
        backtrack(i+1,subset)
        subset.pop()
        
        while i+1<len(arr) and arr[i]==arr[i+1]:
            i+=1
        backtrack(i+1,subset)
    backtrack(0,[])
    return res
