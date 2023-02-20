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

long long n, m;

long long func(long long x, int num){
    long long cnt = 0;
    for (long long i = num; i <= x; i *= num)
        cnt += x / i;
    return cnt;
}

int main(){
    fastio;
    
    cin >> n >> m;
    
    cout << min(func(n, 5) - func(n - m, 5) - func(m, 5), func(n, 2) - func(n - m, 2) - func(m, 2)) << '\n';
    
    return 0;
}
