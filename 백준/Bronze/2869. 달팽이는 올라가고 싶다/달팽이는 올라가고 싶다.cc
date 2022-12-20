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

int a, b, v;
int t = 0;
int cnt = 1;

int main(){
    cin >> a >> b >> v;
    
    cnt += (v - a) / (a - b);
    
    if ((v - a) % (a - b) != 0){
        cnt++;
    }
    
    if (a >= v) cout << 1 << endl;
    else cout << cnt << endl;
    
    return 0;
}