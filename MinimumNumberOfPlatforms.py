from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def calculateMinPatforms(at, dt, n):
    at.sort()
    dt.sort()
    res,count=0,0
    l1,l2=0,0
    
    while l1<n:
        if at[l1]<=dt[l2]:
            l1+=1
            count+=1
            
        else:
            l2+=1
            count-=1
        res=max(res,count)
    return res
             
    

# Taking the input.
def takeInput():
    n = int(stdin.readline().strip())
    at = list(map(int, stdin.readline().strip().split(" ")))
    dt = list(map(int, stdin.readline().strip().split(" ")))

    return at, dt, n

# Main.
T = int(input())
while (T > 0):
    T -= 1
    at, dt, n = takeInput()
    minNumOfPlatforms = calculateMinPatforms(at, dt, n)
    print(minNumOfPlatforms)
