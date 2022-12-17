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

using namespace std;

int main(){
    int a1, b1, a2, b2, a3, b3;
    int cp;
    vector<int> a;
    vector<int> b;
    
    cin >> a1 >> b1;
    cin >> a2 >> b2;
    cin >> a3 >> b3;
    
    a.push_back(a2 - a1);
    a.push_back(b2 - b1);
    
    b.push_back(a3 - a2);
    b.push_back(b3 - b2);
    
    cp = a[0] * b[1] - a[1] * b[0];
    
    if (cp == 0) cout << "0" << endl;
    else if (cp > 0) cout << "1" << endl;
    else cout << "-1" << endl;
    
    return 0;
}
