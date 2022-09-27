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

int main(int argc, const char * argv[]) {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    string num1, sub1 = "", num2, sub2 = "";
    int result1, result2;
    
    cin >> num1 >> num2;
    
    for (int i = 0; i < 3; i++){
        sub1 += num1[3 - i - 1];
        sub2 += num2[3 - i - 1];
    }
    
    result1 = stoi(sub1);
    result2 = stoi(sub2);
    
    if (result1 > result2) cout << result1 << endl;
    else cout << result2 << endl;
    
}
