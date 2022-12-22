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

using namespace std;

int n, n_sub, t, ans = -1;

int main(){
    cin >> n;
    n_sub = n;
    
    if (n % 5 == 0){
        cout << n / 5 << endl;
        return 0;
    }
    
    t = n / 5;
    
    while (t >= 0){
        n -= 5 * t;
                
        if (n % 3 == 0){
            ans = t + n / 3;
            break;
        }
        
        t -= 1;
        n = n_sub;
    }
    
    cout << ans << endl;
    
    return 0;
}