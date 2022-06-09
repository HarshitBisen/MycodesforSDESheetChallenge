#include <bits/stdc++.h> 
int subarraysXor(vector<int> &arr, int x)
{
    map<int,int> m;
    int xorr=0;
    int ans=0;
    for(auto it:arr){
        xorr=xorr^it;
        if(xorr==x){
            ans++;
        }
        if(m.find(xorr^x)!=m.end()){
            ans+=m[xorr^x];
        }
    m[xorr]+=1;
    
    }
return ans;
}
