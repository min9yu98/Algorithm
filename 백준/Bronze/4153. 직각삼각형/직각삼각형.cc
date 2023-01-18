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

int x, y, z;
int arr[3];

int main(){
    fastio;

    while(true){
        cin >> x >> y >> z;
        
        if (x == 0 && y == 0 && z == 0) break;
    
        arr[0] = x; arr[1] = y; arr[2] = z;
        
        sort(arr, arr+3);
        
        if ((arr[0] * arr[0]) + (arr[1] * arr[1]) == (arr[2] * arr[2])) cout << "right" << '\n';
        else cout << "wrong" << '\n';
    }
    
    
    
    return 0;
}
