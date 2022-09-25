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

int main(int argc, const char * argv[]) {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    char spell[1000000];
    string str;
    int cnt = 1;
    cin.getline(spell, 10000000, '\n');
    str = spell;

    if (str.length() == 1 && str[0] == ' ') {
        cout << 0 << endl;
        return 0;
    }
    
    for (int i = 0; i < str.length(); i++){
        if (i == 0 && str[i] == ' ') continue;
        if (i == str.length() - 1 && str[i] == ' ') continue;
        if (str[i] == ' ') cnt ++;
    }
    
    cout << cnt << endl;
    return 0;
}
