def longestSubSeg(arr, n, k):
    maxones=0
    start=0
    zerocount=0
    for end in range(n):
        if arr[end]==0:
            zerocount+=1
        while zerocount>k:
            if arr[start]==0:
                zerocount-=1
            start+=1
        maxones=max(maxones,end-start+1)
    return maxones
      
    
