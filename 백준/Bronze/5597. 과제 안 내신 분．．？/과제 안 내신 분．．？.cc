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

bool c[31] = {false,};

int main(){
    int student;
    for (int i = 0; i < 28; i++){
        cin >> student;
        c[student] = true;
    }
    
    for (int i = 1; i < 31; i++){
        if (c[i] == true){
            continue;
        } else {
            cout << i << endl;
        }
    }
    
    return 0;
}
