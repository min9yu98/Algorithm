#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <ostream>
#include <time.h>

using namespace std;

int main(int argc, const char * argv[]) {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    int total;
    int n;
    int price, cnt;
    
    cin >> total;
    cin >> n;
    
    for (int i = 0; i < n; i++){
        cin >> price >> cnt;
        total -= (price * cnt);
    }
    
    cout << (total == 0 ? "Yes" : "No") << endl;
}
