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

#define PI 3.1415926535897932
int n;

int main(){
    fastio;

    cin >> n;
    
    cout << fixed;
    cout.precision(6);
    cout << n * n * PI << '\n' << n * n * 2 << '\n';
    
    
    return 0;
}
