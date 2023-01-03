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

int n, num;
int arr[10001] = {0};

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n;
    
    for (int i = 0; i < n; i++){
        cin >> num;
        arr[num]++;
    }
    
    for (int i = 1; i <= 10000; i++){
        if (arr[i] == 0) continue;
        else {
            for (int j = 0; j < arr[i]; j++){
                cout << i << '\n';
            }
        }
    }
   
    return 0;
}
