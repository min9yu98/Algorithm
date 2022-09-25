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
    
    int chess[6] = {1, 1, 2, 2, 2, 8};
    int num;
    
    for (int i = 0; i < 6; i++){
        cin >> num;
        cout << chess[i] - num << " ";
    }
    cout << endl;
}
