#include <bits/stdc++.h> 
string fourSum(vector<int> arr, int target, int n) {
    unordered_map<int, vector<pair<int, int> > > hash;
  
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
  
            int sum = arr[i] + arr[j];
            if (hash.find(target - sum) != hash.end()) {
                auto num = hash.find(target - sum);
                vector<pair<int, int> > v = num->second;
  
                for (int k = 0; k < num->second.size(); k++) {
  
                    pair<int, int> it = v[k];
  
                    if (it.first != i && it.first != j && 
                        it.second != i && it.second != j)
                        return "Yes";
                }
            }
  
            hash[sum].push_back(make_pair(i, j));
        }
    }
    hash.clear();
    return "No";
}
