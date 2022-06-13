from typing import List

def fun(index,sum,num,ans):
    if index==len(num):
        ans.append(sum)
        return
    fun(index+1,sum+num[index],num,ans)
    fun(index+1,sum,num,ans)
    

def subsetSum(num: List[int]) -> List[int]:
    # Write your code here.
    ans=[]
    fun(0,0,num,ans)
    ans.sort()
    return ans
