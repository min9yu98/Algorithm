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

int x, y, w, h;

int main(){
    fastio;

    cin >> x >> y >> w >> h;
    
    cout << min(min(abs(x - w), abs(x)), min(abs(y - h), abs(y))) << '\n';
    
    return 0;
}
