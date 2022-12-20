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
    
    int i = 1;
    int cnt = 1;
    
    while (n > i){
        i += (6 * cnt);
        cnt++;
    }
    cout << cnt << endl;
    return 0;
}
