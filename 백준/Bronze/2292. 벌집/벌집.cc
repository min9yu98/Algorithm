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

int n;

int main(){
    cin >> n;
    
    if (n == 1) {
        cout << 1 << endl;
        return 0;
    }
    int i = 0;
    while (true){
        if (2 + 3 * (i * i) - 3 * i <= n && n <= 1 + 3 * (i * i) + 3 * i){
            i++;
            cout << i << endl;
            break;
        }
        i++;
    }
    
    return 0;
}
