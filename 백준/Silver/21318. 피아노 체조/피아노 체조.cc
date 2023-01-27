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

int N, Q, x, y, tmp = 0, m;
int cnt[100001];

int main(){
    fastio;
    
    cin >> N;
    for (int i = 1; i <= N; i++) {
        cin >> m;
        
        if (m < tmp){
            cnt[i] += cnt[i - 1] + 1;
        } else {
            cnt[i] = cnt[i - 1];
        }
        
        tmp = m;
    }
    
    cin >> Q;
    
    for (int i = 0; i < Q; i++){
        cin >> x >> y;
        cout << cnt[y] - cnt[x] << '\n';
    }
    
    
}
