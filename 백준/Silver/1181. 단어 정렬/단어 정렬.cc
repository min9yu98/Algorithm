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

int n;
string str;
vector<string> v;

bool comp(string a, string b){
    if (a.length() == b.length()) return a < b;
    return a.length() < b.length();
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        cin >> str;
        if (find(v.begin(), v.end(), str) == v.end()){
            v.push_back(str);
        }
    }
    
    sort(v.begin(), v.end(), comp);
    
    for (int i = 0; i < v.size(); i++){
        cout << v[i] << '\n';
    }
    
    return 0;
}
