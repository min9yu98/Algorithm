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

int n, m, p = 1;

int main(){
    fastio;
    
    cin >> n >> m;
    
    for (int i = 2; i <= min(n, m); i++){
        if (n % i == 0 && m % i == 0)
            p = max(i, p);
    }
    
    cout << p << '\n' << n / p * m << '\n';
    
    return 0;
}
