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

int n, total = 0;
vector<int> v;

int main(){
    
    for (int i = 0; i < 5; i++){
        cin >> n;
        total += n;
        v.push_back(n);
    }
    
    sort(v.begin(), v.end());
    
    cout << total / 5 << endl << v[2] << endl;
   
    return 0;
}
