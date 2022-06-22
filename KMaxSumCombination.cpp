#include<bits/stdc++.h>
vector<int> kMaxSumCombination(vector<int> &a, vector<int> &b, int n, int k){
	vector<int> ans;
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
 
    priority_queue<pair<int, pair<int, int> > > pq;
 
    set<pair<int, int> > my_set;
 
    pq.push(make_pair(a[n - 1] + b[n - 1],
                      make_pair(n - 1, n - 1)));
 
    my_set.insert(make_pair(n - 1, n - 1));
 
    for (int count = 0; count < k; count++)
    {
        pair<int, pair<int, int> > temp = pq.top();
        pq.pop();
 
        ans.push_back(temp.first);
 
        int i = temp.second.first;
        int j = temp.second.second;
 
        int sum = a[i - 1] + b[j];
 
        pair<int, int> temp1 = make_pair(i - 1, j);
 
        if (my_set.find(temp1) == my_set.end())
        {
            pq.push(make_pair(sum, temp1));
            my_set.insert(temp1);
        }
 
        sum = a[i] + b[j - 1];
        temp1 = make_pair(i, j - 1);
 
        if (my_set.find(temp1) == my_set.end())
        {
            pq.push(make_pair(sum, temp1));
            my_set.insert(temp1);
        }
    }
    return ans;
}
