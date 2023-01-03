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

string num;
int n;
vector<int> v;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> num;
    
    for (int i = 0; i < num.size(); i++){
        v.push_back(num[i] - '0');
    }
    
    sort(v.begin(), v.end());
    reverse(v.begin(), v.end());
    
    for (int i = 0; i < v.size(); i++){
        cout << v[i];
    }
    cout << '\n';
    
    return 0;
}
