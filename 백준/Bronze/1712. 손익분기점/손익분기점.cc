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

using namespace std;

int a, b, c;
int bep;

int main(){
    cin >> a >> b >> c;
    
    if (c - b <= 0) cout << -1 << endl;
    else {
        bep = (a / (c - b)) + 1;
        cout << bep << endl;
    }
    
    return 0;
}
