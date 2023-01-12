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

int n, m, num;
int arr[20000001];

int main(){
    fastio;

    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> num;
        arr[num + 10000000]++;
    }
    
    cin >> m;
    for (int i = 0; i < m; i++){
        cin >> num;
        
        if (arr[num + 10000000] == 0) cout << 0 << ' ';
        else cout << 1 << ' ';
    }
    cout << '\n';
    
    
    return 0;
}
