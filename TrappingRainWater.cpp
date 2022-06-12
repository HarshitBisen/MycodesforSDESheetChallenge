#include <bits/stdc++.h> 
long getTrappedWater(long *arr, int n){
    long maxl[n];
    long maxr[n];
    
    long maxleft=arr[0];
    for(int i=0;i<n;i++){
        if(arr[i]>maxleft) maxleft=arr[i];
        maxl[i]=maxleft;
    }
    
    long maxright=arr[n-1];
    for(int j=n-1;j>=0;j--){
        if(arr[j]>maxright) maxright=arr[j];
        maxr[j]=maxright;
        
    }
    
    long ans=0;
    for(int k=0;k<n;k++){
        long p=min(maxl[k],maxr[k])-arr[k];
        if (p>=0){
            ans+=p;
        }
    }
    return ans;
}
