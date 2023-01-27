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

int N, M, n, m, startx, starty, endx, endy, total;
int arr[1025][1025];
int dp[1025][1025];

int main(){
    fastio;
    
    cin >> N >> M;
    
    for (int i = 1; i <= N; i++){
        for (int j = 1; j <= N; j++){
            cin >> arr[i][j];
            dp[i][j] += dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + arr[i][j];
        }
    }
    
    for (int k = 0; k < M; k++){
        cin >> startx >> starty >> endx >> endy;
        
        cout << dp[endx][endy] - dp[endx][starty - 1] - dp[startx - 1][endy] + dp[startx - 1][starty - 1] << '\n';
    }
    return 0;
}
