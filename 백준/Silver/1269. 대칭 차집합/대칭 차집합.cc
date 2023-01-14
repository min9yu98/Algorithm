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

int N, M, n;
map<int, bool> m;

int main(){
    fastio;

    cin >> N >> M;
    
    for (int i = 0; i < N + M; i++){
        cin >> n;
        
        if (m[n] == true){
            m.erase(n);
        } else{
            m[n] = true;
        }
    }
    
    cout << m.size() << '\n';
    
    return 0;
}
