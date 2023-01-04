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

int n, ans = 1, cnt = 0;
string str;

void palin(int fr, int bck){
    if (fr >= bck || str[fr] != str[bck]){
        cnt++;
        if (str[fr] != str[bck]) ans = 0;
        return;
    }
    
    cnt++;
    palin(fr + 1, bck - 1);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n;
    
    for (int i = 0; i < n; i++){
        cin >> str;
        
        palin(0, str.length() - 1);
        
        cout << ans << ' ' << cnt << '\n';
        cnt = 0;
        ans = 1;
    }
        
    return 0;
}
