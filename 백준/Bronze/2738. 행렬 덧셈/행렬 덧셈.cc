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

int n, m, num;

int main(){
    
    cin >> n >> m;
    
    int** arr;
    arr = new int* [n];
    
    for (int i = 0; i < n; i++){
        arr[i] = new int[m];
    }

    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            cin >> num;
            arr[i][j] = num;
        }
    }
    
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            cin >> num;
            arr[i][j] += num;
        }
    }
    
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            cout << arr[i][j] << " ";
        }
        cout << '\n';
    }
    
    return 0;
}
// 동적할당 연습