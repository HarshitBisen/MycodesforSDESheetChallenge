def removeDuplicates(arr,n):
    count=0
    for i in range(1,n):
        if arr[i]==arr[i-1]:
            count+=1
    return len(arr)-count
