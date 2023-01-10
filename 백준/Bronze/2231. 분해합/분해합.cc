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

int num, total, part;

int main(){
    fastio;

    cin >> num;
    
        
    for (int i = 1; i < num; i++){
        total = i;
        part = i;
        
        while(part){
            total += part % 10;
            part /= 10;
        }
        
        if (total == num){
            cout << i << '\n';
            return 0;
        }
    }
    
    cout << 0 << '\n';

    return 0;
}
