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
    int down, up;
    int total = 0;
    int max = 0;
    
    for (int i = 0; i < 10; i++){
        cin >> down >> up;
        total += up - down;
        if (max < total) max = total;
    }
    cout << max << endl;
}
