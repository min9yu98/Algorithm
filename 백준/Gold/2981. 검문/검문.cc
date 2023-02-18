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

int n, m, gcd;
vector<int> v;
vector<int> result;

int GCD(int a, int b){
    if (a % b == 0) return b;
    return GCD(b, a % b);
}

int main(){
    fastio;
    
    cin >> n;
    
    for (int i = 0; i < n; i++){
        cin >> m;
        v.push_back(m);
    }
    sort(v.begin(), v.end());
    
    gcd = v[1] - v[0];
    for (int i = 2; i < n; i++){
        gcd = GCD(gcd, v[i] - v[i - 1]);
    }
    for (int i = 2; i * i <= gcd; i++){
        if (gcd % i == 0){
            result.push_back(i);
            result.push_back(gcd / i);
        }
    }
    result.push_back(gcd);
    sort(result.begin(), result.end());
    result.erase(unique(result.begin(), result.end()), result.end());
    
    for (int i = 0; i < result.size(); i++){
        cout << result[i] << " ";
    }
    cout << '\n';
    
    return 0;
}
