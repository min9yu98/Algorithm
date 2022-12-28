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

#define MAX 123456 * 2 + 1

int n, cnt;
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
    
    while(true){
        cnt = 0;
        cin >> n;
        
        if (n == 0) break;
        
        for (int i = n + 1; i <= 2 * n; i++){
            if (arr[i] != 0) cnt++;
        }
        
        cout << cnt << '\n';
    }

    return 0;
}
