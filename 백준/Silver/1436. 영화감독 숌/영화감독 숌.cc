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
string ending = "666";

int main(){
    fastio;

    cin >> n;
    
    for (int i = 1; i <= 1000000000; i++){
        string tmp = to_string(i);
        if (tmp.find(ending) != string::npos){
            cnt++;
        }
        
        if (cnt == n){
            cout << i << '\n';
            break;
        }
    }
    
    return 0;
}
