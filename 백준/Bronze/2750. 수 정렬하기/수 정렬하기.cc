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

int n, num;
vector<int> v;

int main(){
    
    cin >> n;
    
    for (int i = 0; i < n; i++){
        cin >> num;
        v.push_back(num);
    }
    
    sort(v.begin(), v.end());
    
    for (int i = 0; i < n; i++){
        cout << v[i] << endl;
    }
   
    return 0;
}
