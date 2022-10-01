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
string alpha[8] = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};

int main(int argc, const char * argv[]) {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    cin >> str;

    for (int i = 0; i < 8; i++){
        while(1){
            if (str.find(alpha[i]) == string::npos) break;
            str.replace(str.find(alpha[i]), alpha[i].length(), "*");
        }
    }
    cout << str.length() << endl;
    
}
