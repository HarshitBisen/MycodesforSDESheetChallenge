#include<bits/stdc++.h>

bool comparator(pair<int,int>a,pair<int,int>b){
    double r1=(double)a.second/(double)a.first;
    double r2=(double)b.second/(double)b.first;
    return r1>r2;
}

double maximumValue (vector<pair<int, int>>& items, int n, int w)
{
    sort(items.begin(),items.end(),comparator);
    int curweight=0;
    double finalw=0.0;
    
    for(int i=0;i<n;i++){
        if(curweight+items[i].first<=w){
            curweight+=items[i].first;
            finalw+=items[i].second;
        }
        else{
            int rem=w-curweight;
            finalw+=((double)items[i].second/(double)items[i].first)*(double)rem;
            break;
            
        }
    }
    return finalw;
}
