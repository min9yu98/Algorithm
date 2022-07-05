#include <iostream>

using namespace std;

int main(int argc, char const *argv[]){
    int h, m, total;
    cin >> h >> m;
    
    total = h * 60 + m;
    
    if (total - 45 < 0) {
        total = 24 * 60 + (total - 45);
    } else {
        total -= 45;
    }
    
    cout << total / 60 << " " << total % 60;
    
}

