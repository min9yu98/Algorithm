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

int a, b, cnt = 0;
string s;
map<string, bool> m;

int main(){
    fastio;

    cin >> a >> b;
    for (int i = 0; i < a; i++){
        cin >> s;
        m[s] = true;
    }
    for (int i = 0; i < b; i++){
        cin >> s;

        if (m[s]) cnt++;
    }
    
    cout << cnt << '\n';
    
    return 0;
}
