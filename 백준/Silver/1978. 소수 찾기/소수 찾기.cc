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

int n, cnt = 0;
bool checking[1001] = {1, 1};

void check_prime(){
    for (int i = 2; i * i <= 1001; i++){
        if (checking[i]) continue;
        
        for (int j = i * i; j < 1001; j += i) checking[j] = 1;
    }
}

int main(){
    check_prime();
    cin >> n;
    
    int k;
    for (int i = 0; i < n; i++){
        cin >> k;
        if (!checking[k]) cnt++;
    }

    cout << cnt << endl;
    return 0;
}
