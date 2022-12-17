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

int n;
vector<int> v;
int f;

int main(){
    cin >> n;
    
    int num;
    for (int i = 0; i < n; i++){
        cin >> num;
        v.push_back(num);
    }
    
    cin >> f;
    
    cout << count(v.begin(), v.end(), f);
    
    return 0;
}
