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

int n;

int fib(int n) {
    if (n == 1 || n == 2){
        return 1;
    }
    return fib(n - 1) + fib(n - 2);
}

int main(int argc, const char * argv[]) {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    cin >> n;
    
    cout << fib(n) << " " << n - 2 <<  endl;
}
