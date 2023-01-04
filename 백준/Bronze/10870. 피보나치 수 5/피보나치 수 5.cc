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

using namespace std;

int n, ans;

int fib(int x){
    if (x <= 0) return 0;
    else if (x == 1) return 1;
    
    return fib(x - 1) + fib(x - 2);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n;
    
    ans = fib(n);
    
    cout << ans << '\n';
    
    return 0;
}
