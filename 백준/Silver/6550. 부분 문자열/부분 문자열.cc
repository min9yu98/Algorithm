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

string s1, s2;
int idx;
bool check;

int main(){
    fastio;
        
    while (cin >> s1 >> s2){
        check = false;
        idx = 0;
        for (int i = 0; i < s2.length(); i++){
            if (s1[idx] == s2[i])
                idx++;
            if (idx == s1.length()){
                check = true;
                break;
            }
        }
        
        if (check)
            cout << "Yes" << '\n';
        else
            cout << "No" << '\n';
    }
    
    return 0;
}
