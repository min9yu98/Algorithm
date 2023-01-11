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

string wb[8] = {
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
};
string bw[8] = {
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB"
};
string board[50];
int n, m, min_val = 99999;

int WB_cnt(int x, int y){
    int cnt = 0;
    for (int i = 0; i < 8; i++){
        for (int j = 0; j < 8; j++){
            if (board[i + x][j + y] != wb[i][j])
                cnt++;
        }
    }
    return cnt;
}

int BW_cnt(int x, int y){
    int cnt = 0;
    for (int i = 0; i < 8; i++){
        for (int j = 0; j < 8; j++){
            if (board[i + x][j + y] != bw[i][j])
                cnt++;
        }
    }
    return cnt;
}

int main(){
    fastio;

    cin >> n >> m;
    
    for (int i = 0; i < n; i++){
        cin >> board[i];
    }
    
    for (int i = 0; i + 8 <= n; i++){
        for (int j = 0; j + 8 <= m; j++){
            int tmp;
            tmp = min(WB_cnt(i, j), BW_cnt(i, j));
            if (tmp < min_val){
                min_val = tmp;
            }
        }
    }
    cout << min_val << '\n';
    return 0;
}
