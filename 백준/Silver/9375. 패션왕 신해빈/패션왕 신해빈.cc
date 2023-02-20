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

int n, clth, cnt;
string c, cat;

int main(){
    fastio;
    
    cin >> n;
    for (int z = 0; z < n; z++){
        cin >> clth;
        cnt = 1;
        
        set<string> cats;
        map<string, int> m;
        for (int q = 0; q < clth; q++){
            cin >> c >> cat;
            m[cat] += 1;
            cats.insert(cat);
        }

        for (auto s: cats){
            cnt *= (m[s] + 1);
        }
        cout << cnt - 1 << '\n';
    }

    return 0;
}
