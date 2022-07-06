def pwset(v):
    # Write your code here
    # Return a 2-D list containing all subsets
    ans=[]
    cur=[]
    def backtrack(index):
        if index>=len(v):
            ans.append(cur.copy())
            return
        cur.append(v[index])
        backtrack(index+1)
        
        cur.pop()
        backtrack(index+1)
        
    backtrack(0)
    return ans
        
         
