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

int x, front, back, n = 1, son, mom;

int main(){
    cin >> x;
    
    while (true){
        front = (n * n - n + 2) / 2;
        back = (n * n + n) / 2;
        
        if (x >= front && x <= back){
            for (int i = 0; i < back - front + 1; i++){
                if (i + front == x){
                    if (n % 2 == 0){
                        cout << i + 1 << "/" << (n + 1) - (i + 1) << endl;
                    } else {
                        cout << (n + 1) - (i + 1) << "/" << i + 1 << endl;
                    }
                    break;
                }
            }
            break;
        }
        n += 1;
    }
    
    return 0;
}
