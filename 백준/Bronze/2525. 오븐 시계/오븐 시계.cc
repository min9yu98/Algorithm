#include <iostream>

using namespace std;

int main(int argc, char const *argv[]){
    int h, m, c, total;
    cin >> h >> m >> c;
    
    total = h * 60 + m + c;
    
    cout << total / 60 % 24 << " " << total % 60 << endl;
    
    
}

