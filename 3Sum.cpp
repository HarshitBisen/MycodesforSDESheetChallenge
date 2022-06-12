#include <bits/stdc++.h> 
vector<vector<int>> findTriplets(vector<int>arr, int n, int K) {
	sort(arr.begin(),arr.end());
    vector<vector<int>> ans;
    
    for(int i=0;i+2<n;i++){
        int left= i+1;     
        int right= n-1;     
        
        while(left<right){
            int sum= arr[i]+arr[left]+arr[right];
            if(sum==K){
                ans.push_back({arr[i],arr[left],arr[right]});
                int left_element=arr[left];
                int right_element=arr[right];
                while(left<right && arr[left]==left_element)left++;        
                while(left<right && arr[right]==right_element)right--;     
            }
            
            else if(sum<K)left++;  
            
            else right--;          
            
            while(i+1<n && arr[i]==arr[i+1])i++;  
            
        }
    }
    return ans;
}
