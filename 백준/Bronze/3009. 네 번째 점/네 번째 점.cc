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

int x, y;
bool x_arr[1001];
bool y_arr[1001];

int main(){
    fastio;

    for (int i = 0; i < 3; i++){
        cin >> x >> y;
        
        if (!x_arr[x]) x_arr[x] = true;
        else x_arr[x] = false;
        
        if (!y_arr[y]) y_arr[y] = true;
        else y_arr[y] = false;
    }
    
    for (int i = 0; i < 1001; i++){
        if (x_arr[i]) x = i;
        if (y_arr[i]) y = i;
    }
    
    cout << x << ' ' << y << '\n';
    
    
    
    return 0;
}
