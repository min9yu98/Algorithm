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

int T, n, m, a, b, c;

int main(){
    fastio;
    
    cin >> T;
    
    for (int i = 0; i < T; i++){
        cin >> n >> m;
        a = max(n, m);
        b = min(n, m);
        c = a % b;
        while (c != 0){
            a = b;
            b = c;
            c = a % b;
        }
        
        cout << (n * m) / b << '\n';
    }
    
    return 0;
}
