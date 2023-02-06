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

string s, s1;
string arr[20];
int n;

int main(){
    fastio;
    
    
    cin >> s >> n;
    
    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }
    
    for (int i = 0; i < 26; i++){
        s1 = "";
        for (int j = 0; j < s.length(); j++){
            s1 += ((s[j] - 'a'+ i) % 26 + 'a');
        }
        
        for (int k = 0; k < n; k++){
            if (s1.find(arr[k]) != string::npos){
                cout << s1 << '\n';
                return 0;
            }
        }
    }
    
    return 0;
}
