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

int n, dif, maxim = -1, x, y, ans;

int main(){
    
    for (int i = 1; i <= 81; i++){
        cin >> n;
        if (maxim < n){
            ans = n;
            if (i % 9 == 0){
                x = i / 9;
                y = 9;
            } else {
                x = i / 9 + 1;
                y = i % 9;
            }
            maxim = n;
        }
    }
    
    cout << ans << endl << x << " " << y << endl;
    
    return 0;
}
