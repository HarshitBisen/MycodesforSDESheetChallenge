#include <bits/stdc++.h>
struct format{
    int deadline;
    int profit;
};

bool comparator(struct format f1,format f2){
    return f1.profit>f2.profit;
}

int jobScheduling(vector<vector<int>> &jobs)
{
    int n=jobs.size();
    struct format job[n];
    for(int i=0;i<n;i++){
        job[i].deadline=jobs[i][0];
        job[i].profit=jobs[i][1];
        }
    sort(job,job+n,comparator);
    int max_deadline=0;
    for(int j=0;j<n;j++){
        max_deadline=max(max_deadline,job[j].deadline);
    }
    int maxprofit=0;
    vector<int> filled(max_deadline+1,-1);
    for(int i=0;i<n;i++){
        for(int j=job[i].deadline;j>0;j--){
            if(filled[j]==-1){
                filled[j]=0;
                maxprofit+=job[i].profit;
                break;
            }
        }
    }
    return maxprofit;
    
    
}
