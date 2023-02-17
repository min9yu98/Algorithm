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

int T, n, startx, starty, endx, endy, cnt;
int x, y, r;

int main(){
    fastio;
    
    cin >> T;

    for (int k = 0; k < T; k++){
        cnt = 0;
        cin >> startx >> starty >> endx >> endy >> n;
        for (int i = 0; i < n; i++){
            cin >> x >> y >> r;
            if ((pow((startx - x), 2) + pow((starty - y), 2)) <= pow(r, 2) || (pow((endx - x), 2) + pow((endy - y), 2)) <= pow(r, 2)){
                if ((pow((startx - x), 2) + pow((starty - y), 2)) <= pow(r, 2) && (pow((endx - x), 2) + pow((endy - y), 2)) <= pow(r, 2))
                    continue;
                cnt++;
            }
        }
        
        cout << cnt << '\n';
    }
    
    return 0;
}
