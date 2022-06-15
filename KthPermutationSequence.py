def kthPermutation(n, k):
    fact=[1]*n
    dig=[1]*n
    for i in range(1,n):
        fact[i]=fact[i-1]*(i+1)
        dig[i]=i+1
        
    ans=""
    while len(ans)<n-1:
        repeat=fact[-2]
        next_dig=(k-1)//repeat
        ans+=str(dig[next_dig])
        dig.pop(next_dig)
        fact=fact[:-1]
        k=k%repeat
        if k==0:
            for i in range(len(dig)-1,-1,-1):
                ans+=str(dig[i])
    if len(ans)<n:
        ans+=str(dig[0])
        
        
    
    
    
    
    return ans
        
