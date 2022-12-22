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

int stair[15][15];
int t, k, n;

int main(){
    
    for (int i = 0; i < 15; i++) stair[0][i] = i;
    
    cin >> t;
    
    for (int i = 0; i < t; i++){
        cin >> k >> n;
        
        for (int j = 1; j <= k; j++){
            for (int x = 1; x <= n; x++){
                stair[j][x] = stair[j][x - 1] + stair[j - 1][x];
            }
        }
        
        cout << stair[k][n] << endl;
    }
}