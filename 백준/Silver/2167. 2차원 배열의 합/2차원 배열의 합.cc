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
int arr[301][301];

int main(){
    fastio;
    
    cin >> N >> M;
    
    for (int i = 1; i <= N; i++){
        for (int j = 1; j <= M; j++){
            cin >> m;
            arr[i][j] = m;
        }
    }
    
    cin >> n;
    for (int k = 0; k < n; k++){
        total = 0;
        
        cin >> startx >> starty >> endx >> endy;
        
        for (int i = startx; i <= endx; i++){
            for (int j = starty; j <= endy; j++){
                total += arr[i][j];
            }
        }
        cout << total << '\n';
    }
    return 0;
}
