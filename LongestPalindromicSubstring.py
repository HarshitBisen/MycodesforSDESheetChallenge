def longestPalinSubstring(str):
    ans=""
    res=0
    
    for i in range(len(str)):
        l,r=i,i
        while l>=0 and r<len(str) and str[l]==str[r]:
            if r-l+1>res:
                res=r-l+1
                ans=str[l:r+1]
            l-=1
            r+=1
        l,r=i,i+1
        while l>=0 and r<len(str) and str[l]==str[r]:
            if r-l+1>res:
                res=r-l+1
                ans=str[l:r+1]
            l-=1
            r+=1
    return ans
        
            
