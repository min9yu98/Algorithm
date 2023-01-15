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

set<string> s;
string str, x;
int a, b;

int main(){
    fastio;

    cin >> str;
    a = 0; b = 1;
    
    for (int i = 0; i < str.length(); i++){
        x = "";
        for (int j = i; j < str.length(); j++){
            x += str[j];
            s.insert(x);
        }
    }
    
    cout << s.size() << '\n';
    
    return 0;
}
