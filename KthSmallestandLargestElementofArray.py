def kthSmallLarge(arr, n, k):
    arr.sort()
    ans=[]
    ans.append(arr[k-1])
    ans.append(arr[n-k])
    return ans
