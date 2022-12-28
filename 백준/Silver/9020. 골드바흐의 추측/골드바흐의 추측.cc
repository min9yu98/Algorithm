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

using namespace std;

#define MAX 10001

int n, m, p, tmp, dif, ans1, ans2;
int arr[MAX] = {0, };

void prime(){
    for (int i = 2; i <= MAX; i++){
        arr[i] = i;
    }
    
    for (int i = 2; i <= sqrt(MAX); i++){
        if (arr[i] == 0) continue;
        
        for (int j = i * i; j <= MAX; j += i){
            arr[j] = 0;
        }
    }
    
}

int main(){
    prime();
    
    cin >> n;
   
    for (int i = 0; i < n; i++){
        cin >> m;
        p = 2;
        dif = 10001;
        while (m > p){
            tmp = m;
            m -= p;
            
            if (arr[p] != 0 && arr[m] != 0){
                if (min(dif, abs(p - arr[m])) == abs(p - arr[m])){
                    dif = abs(p - arr[m]);
                    ans1 = min(p, arr[m]);
                    ans2 = max(p, arr[m]);
                }
            }
            
            m = tmp;
            p++;
        }
        
        cout << ans1 << " " << ans2 << '\n';
    }
    

    return 0;
}
