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

int n, k, num;
vector<int> v;

int main(){
    
    cin >> n >> k;
    
    for (int i = 0; i < n; i++){
        cin >> num;
        v.push_back(num);
    }
    
    sort(v.begin(), v.end());
    
    cout << v[v.size() - k] << endl;
   
    return 0;
}
