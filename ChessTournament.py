def canplace(positions,n,c,mid):
    coor=positions[0]
    count=1
    for i in range(1,n):
        if positions[i]-coor>=mid:
            count+=1
            coor=positions[i]
        if c==count:
            return True
    return False





def chessTournament(positions, n , c):
    positions.sort()
    res=0
    low,high=1,positions[n-1]-positions[0]
    while low<=high:
        mid=(low+high)//2
        if canplace(positions,n,c,mid):
            res=mid
            low=mid+1
        else:
            high=mid-1
    return res
            
