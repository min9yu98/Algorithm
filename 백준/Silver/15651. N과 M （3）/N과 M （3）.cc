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

int n, m;
int arr[9];
bool visited[9];

void dfs(int cnt){
    if (cnt == m){
        for (int i = 0; i < m; i++)
            cout << arr[i] << ' ';
        cout << '\n';
        return;
    }
    
    for (int i = 1; i <= n; i++){
        arr[cnt] = i;
        dfs(cnt + 1);
    }
}

int main(){
    fastio;
    
    cin >> n >> m;
    
    dfs(0);
    
    return 0;
}
