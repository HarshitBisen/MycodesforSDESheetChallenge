#include <bits/stdc++.h> 
int findDuplicate(vector<int> &arr, int n){
	// Write your code here.
    int slow=arr[0];
    int fast=arr[0];
    do{
        slow=arr[slow];
        fast=arr[arr[fast]];
    }while(slow!=fast);
    
    int slow2=arr[0];
    while(slow!=slow2){
        slow=arr[slow];
        slow2=arr[slow2];
    }
    return slow;
}
