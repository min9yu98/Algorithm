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

vector<pair<int, int>> vp;
int n, x, y;

bool comp(pair<int, int> a, pair<int, int> b){
    if (a.second == b.second){
        return a.first < b.first;
    } else {
        return a.second < b.second;
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        cin >> x >> y;
        vp.push_back(pair<int, int>(x, y));
    }
    
    sort(vp.begin(), vp.end(), comp);
    
    for (int i = 0; i < n; i++){
        cout << vp[i].first << " " << vp[i].second << '\n';
    }
    
    return 0;
}
