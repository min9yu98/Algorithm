#include <stdio.h>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <ostream>
#include <string>
#include <cstring>
#include <sstream>
#include <time.h>
#include <queue>
#include <cstdlib>
#include <stdbool.h>
#include <map>

using namespace std;

int n, age;
string name;
vector<pair<int, string>> vp;
pair<int, string> p;

bool comp(pair<int, string> a, pair<int, string> b){
    return a.first < b.first;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n;
    
    for (int i = 0; i < n; i++){
        cin >> p.first >> p.second;
        vp.push_back(p);
    }
    
    stable_sort(vp.begin(), vp.end(), comp);
    
    for (int i = 0; i < n; i++){
        cout << vp[i].first << " " << vp[i].second << '\n';
    }
    
    return 0;
}
