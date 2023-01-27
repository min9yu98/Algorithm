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

#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
using namespace std;

long n, m, i = 0, j = 0, total = 0, summ = 0, summ2 = 0;
vector<long> v;

int main(){
    fastio;
    
    cin >> n;
        
    for (int i = 0; i < n; i++){
        cin >> m;
        summ += m;
        v.push_back(m);
    }
    
    for (int i = 0; i < n; i++){
        summ2 += v[i] * v[i];
    }
    
    cout << ((summ * summ) - summ2) / 2 << '\n';
    
    return 0;
}
