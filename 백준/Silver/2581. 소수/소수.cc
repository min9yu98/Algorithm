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

int m, n, total = 0, min_prime = 10001;
bool checking[10001] = {1, 1};

void check_prime(){
    for (int i = 2; i * i <= 10001; i++){
        if (checking[i]) continue;
        
        for (int j = i * i; j < 10001; j += i) checking[j] = 1;
    }
}

int main(){
    check_prime();
    cin >> m >> n;
    
    for (int i = m; i <= n; i++){
        if (!checking[i]) {
            total += i;
            min_prime = min(i, min_prime);
        }
    }

    if (min_prime == 10001){
        cout << -1 << endl;
    } else {
        cout << total << endl << min_prime << endl;
    }
    return 0;
}
