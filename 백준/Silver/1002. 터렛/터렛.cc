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

int n, x, y, r1, a, b, r2, d, cond1, cond2;

int main(){
    fastio;

    cin >> n;
    
    for (int i = 0; i < n; i++){
        cin >> x >> y >> r1 >> a >> b >> r2;
        
        d = (x - a) * (x - a) + (y - b) * (y - b);
        cond1 = (r1 - r2) * (r1 - r2);
        cond2 = (r1 + r2) * (r1 + r2);
        
        if (d == 0){
            if (cond1 == 0) cout << -1 << '\n';
            else cout << 0 << '\n';
        } else if (cond1 == d || cond2 == d) cout << 1 << '\n';
        else if (cond1 < d && d < cond2) cout << 2 << '\n';
        else cout << 0 << '\n';
    }
    
    
    return 0;
}
