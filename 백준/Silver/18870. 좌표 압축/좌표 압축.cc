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

int n, x, y;
vector<int> num;
vector<int> v;
vector<int> idx;
pair<int, int> p;

bool comp(pair<int, string> a, pair<int, string> b){
    return a.first < b.first;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n;
    
    for (int i = 0; i < n; i++){
        cin >> x;
        
        v.push_back(x);
        num.push_back(x);
    }
    
    sort(num.begin(), num.end());
    num.erase(unique(num.begin(), num.end()), num.end());
    
    for (int i = 0; i < n; i++){
        auto it = lower_bound(num.begin(), num.end(), v[i]);
        cout << it - num.begin() << ' ';
    }
    cout << '\n';
    
    return 0;
}
