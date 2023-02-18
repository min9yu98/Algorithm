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

int n, k;

int mul(int a){
    int x = 1;
    for (int i = 1; i <= a; i++){
        x *= i;
    }
    return x;
}

int main(){
    fastio;
    
    cin >> n >> k;
    
    cout << mul(n) / (mul(k) * mul(n - k)) << '\n';
    
    return 0;
}
