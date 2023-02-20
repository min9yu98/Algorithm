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

int n, cnt = 0;

int main(){
    fastio;
    
    cin >> n;
    
    for (int i = 5; i <= n; i *= 5)
        cnt += n / i;
    
    cout << cnt << '\n';
    
    return 0;
}
