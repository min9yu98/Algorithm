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

int n, m;

int main(){
    fastio;

    while (true){
        cin >> n >> m;
        
        if (n == 0 && m == 0) break;
        
        if (n > m){
            if (n % m == 0)
                cout << "multiple" << '\n';
            else
                cout << "neither" << '\n';
        } else {
            if (m % n == 0)
                cout << "factor" << '\n';
            else
                cout << "neither" << '\n';
        }
    }
    
    
    return 0;
}
