#include <bits/stdc++.h> 
    typedef long long lg;
    lg ans=0;
void merge(lg arr[],lg l,lg mid,lg h){
        lg n1=mid-l+1;
        lg n2=h-mid;
        lg arr1[n1],arr2[n2];
        for(lg i=0;i<n1;i++) arr1[i]=arr[l+i];
        for(lg i=0;i<n2;i++) arr2[i]=arr[mid+1+i];
        lg i=0,j=0,k=l;
        while(i<n1 && j<n2){
            if(arr1[i]<=arr2[j]) arr[k++]=arr1[i++];
            else{
                ans+=n1-i;
                arr[k++]=arr2[j++];
            }
        }
        while(i<n1) arr[k++]=arr1[i++];
        while(j<n2) arr[k++]=arr2[j++];
    }

    void mergesort(lg arr[],lg l,lg h){
        if(h>l){
            lg mid=l+(h-l)/2;
            mergesort(arr,l,mid);
            mergesort(arr,mid+1,h);
            merge(arr,l,mid,h);
        }
    }
    
    long long getInversions(long long *arr, int n){
    // Write your code here.
        ans=0;
        mergesort(arr,0,n-1);
        return ans;
    }

