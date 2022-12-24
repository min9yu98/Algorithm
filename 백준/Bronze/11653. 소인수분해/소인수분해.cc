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

int n;

int main(){
    cin >> n;
    
    if (n == 1) return 0;
    
    for (int i = 2; i <= n; i++){
        while (n % i == 0){
            cout << i << endl;
            n /= i;
        }
    }
}
