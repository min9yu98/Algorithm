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

#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
using namespace std;

int n, m, cnt = 0;
string str;
map<string, bool> mp;
vector<string> v;

int main(){
    fastio;

    cin >> n >> m;
    for (int i = 0; i < n; i++){
        cin >> str;
        mp[str] = true;
    }
    
    for (int i = 0; i < m; i++){
        cin >> str;
        
        if (mp[str]){
            v.push_back(str);
            cnt++;
        }
    }
    
    cout << cnt << '\n';
    sort(v.begin(), v.end());
    for (auto s: v){
        cout << s << '\n';
    }
    
    
    return 0;
}
