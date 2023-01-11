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

int n, w, h, cnt = 1, tmp = 0;
vector<pair<int, int>> vp;

int main(){
    fastio;

    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> w >> h;
        vp.push_back(pair<int, int> (w, h));
    }
    
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (i != j){
                if (vp[j].first > vp[i].first && vp[j].second > vp[i].second){
                    cnt++;
                } else if (vp[j].first > vp[i].first && vp[j].second < vp[i].second){
                    tmp = cnt;
                    tmp++;
                } else if (vp[j].first < vp[i].first && vp[j].second > vp[i].second){
                    tmp = cnt;
                    tmp++;
                }
            }
        }
        cout << cnt << " ";
        tmp = 0;
        cnt = 1;
    }
    cout << '\n';

    return 0;
}
