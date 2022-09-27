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

using namespace std;

string str;
int cnt = 0;

void solve(int i){
    if(str[i] >= 65 && str[i] <= 67) cnt += 3;
    else if(str[i] >= 68 && str[i] <= 70) cnt += 4;
    else if(str[i] >= 71 && str[i] <= 73) cnt += 5;
    else if(str[i] >= 74 && str[i] <= 76) cnt += 6;
    else if(str[i] >= 77 && str[i] <= 79) cnt += 7;
    else if(str[i] >= 80 && str[i] <= 83) cnt += 8;
    else if(str[i] >= 84 && str[i] <= 86) cnt += 9;
    else cnt += 10;
}

int main(int argc, const char * argv[]) {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    cin >> str;
    
    for (int i = 0; i < str.length(); i++){
        solve(i);
    }
    cout << cnt << endl;
}
