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

using namespace std;

int main(){
    int n;

    while(cin >> n){
        int num = 0;
        for (int i = 1;i <= n; i ++){
            num = num * 10 + 1;
            num %= n;
            if (num == 0){
                cout << i << endl;
                break;
            }
        }
    }
    
}
