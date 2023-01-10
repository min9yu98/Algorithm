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

int n, m, diff, ans, mini = 300001;
int arr[101];

int main(){
    fastio;

    cin >> n >> m;
    
    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }
    
    for (int i = 0; i < n - 2; i++){
        for (int j = i + 1; j < n - 1; j++){
            for (int k = j + 1; k < n; k++){
                diff = m - (arr[i] + arr[j] + arr[k]);
                if (diff < mini && diff >= 0){
                    mini = diff;
                    ans = arr[i] + arr[j] + arr[k];
                }
            }
        }
    }

    cout << ans << '\n';

    return 0;
}
