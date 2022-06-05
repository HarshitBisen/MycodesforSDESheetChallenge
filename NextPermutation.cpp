#include <bits/stdc++.h> 
vector<int> nextPermutation(vector<int> &permutation, int n)
{
    //  Write your code here.
        int index1;
        int index2;
        for(index1=n-2;index1>=0;index1--){
            if(permutation[index1+1]>permutation[index1]){
                break;
            }
        }
        
        if(index1<0){
            reverse(permutation.begin(),permutation.end());
        }
        else{
        
        for(index2=n-1;index2>index1;index2--){
            if(permutation[index2]>permutation[index1]){
                break;
            }
        }
        
        swap(permutation[index1],permutation[index2]);
        reverse(permutation.begin()+index1+1,permutation.end());
        }
    return permutation;
}
