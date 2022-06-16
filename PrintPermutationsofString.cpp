void func(int l, string &s,vector<string>&ans){
    if(l==s.size()){
        ans.push_back(s);
        return;
    }
    for(int i=l;i<s.size();i++){
        swap(s[l],s[i]);
        func(l+1,s,ans);
        swap(s[l],s[i]);
    }
}


vector<string> findPermutations(string &s) {
    vector<string> ans;
    int l=0;
    func(l,s,ans);
    return ans;
    
}
