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

int n, m, first, gcd;
vector<int> v;

int GCD(int a, int b){
    if (a % b == 0) return b;
    return GCD(b, a % b);
}

int main(){
    fastio;
    
    cin >> n >> first;
    for (int i = 0; i < n - 1; i++){
        cin >> m;
        if (first % m == 0){
            cout << first / m << '/' << 1 << '\n';
        } else {
            gcd = GCD(max(first, m), min(first, m));
            cout << first / gcd << '/' << m / gcd << '\n';
        }
    }
    
    return 0;
}
