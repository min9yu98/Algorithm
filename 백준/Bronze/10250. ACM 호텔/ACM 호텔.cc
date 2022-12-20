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

int t, h, w, n;

int main(){
    cin >> t;
    
    for (int i = 0; i < t; i++){
        int ho = 1, floor;
        cin >> h >> w >> n;
        
        ho += n / h;
        floor = n % h;
        if (n % h == 0) {
            ho--;
            floor = h;
        }
        
        cout << floor * 100 + ho << endl;
    }
}