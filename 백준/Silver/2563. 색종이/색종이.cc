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

int n, x, y, cnt = 0;
int arr[100][100];

int main(){
    
    cin >> n;
    
    while (n--){
        cin >> x >> y;
        
        for (int i = y; i < y + 10; i++){
            for (int j = x; j < x + 10; j++){
                if (!arr[i][j]){
                    cnt++;
                    arr[i][j] = 1;
                }
            }
        }
    }
    
    cout << cnt << endl;
   
    return 0;
}
