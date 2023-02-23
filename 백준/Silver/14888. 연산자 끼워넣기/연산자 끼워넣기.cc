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

int oper[4] = {0, 0, 0, 0};
int n, maxi = -1000000001, mini = 1000000001;
int v[11];

void dp(int result, int idx){
    if (idx == n){
        if (result > maxi)
            maxi = result;
        if (result < mini)
            mini = result;
        return;
    }
    
    for (int i = 0; i < 4; i++){
        if (oper[i] != 0) {
            oper[i]--;
            if (i == 0)
                dp(result + v[idx], idx + 1);
            else if (i == 1)
                dp(result - v[idx], idx + 1);
            else if (i == 2)
                dp(result * v[idx], idx + 1);
            else if (i == 3)
                dp(result / v[idx], idx + 1);
            oper[i]++;
        }
    }
}

int main(){
    fastio;
    
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> v[i];
    
    for (int i = 0; i < 4; i++)
        cin >> oper[i];
    
    dp(v[0], 1);
    
    cout << maxi << '\n' << mini << '\n';
    
    return 0;
}
