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

int n, k;
int dp[1001][1001];

int main(){
    fastio;
    
    cin >> n >> k;
    
    dp[0][0] = 1;
    dp[1][0] = 1;
    dp[1][1] = 1;
    
    for (int i = 2; i <= n; i++){
        for (int j = 0; j <= i; j++){
            if (j == 0) dp[i][0] = 1;
            else if (i == j) dp[i][j] = 1;
            else dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % 10007;
        }
    }
    
    cout << dp[n][k] << '\n';
    
    return 0;
}
