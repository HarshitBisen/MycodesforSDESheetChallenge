def combinationSum2(arr, n, target):
    arr.sort()
    res=[]
    def backtrack(cur,pos,target):
        if target==0:
            res.append(cur.copy())
        if target<=0:
            return
        prev=-1
        for i in range(pos,n):
            if arr[i]==prev:
                continue
            cur.append(arr[i])
            backtrack(cur,i+1,target-arr[i])
            cur.pop()
            prev=arr[i]
    backtrack([],0,target)
    return res
            
        
