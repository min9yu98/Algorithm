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

int n, tmp, result, maxi = 1;
pair<int, int> p[6];

int main(){
    fastio;

    cin >> n;
    
    for (int i = 0; i < 6; i++){
        cin >> p[i].first >> p[i].second;
    }
    
    for (int i = 0; i < 6; i++){
        tmp = p[i].second * p[(i + 1) % 6].second;
        if (maxi == 1 || tmp > maxi){
            maxi = tmp;
            result = (maxi - p[(i + 3) % 6].second * p[(i + 4) % 6].second) * n;
        }
    }
    
    cout << result << '\n';
    
    return 0;
}
