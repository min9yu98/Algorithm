#include <iostream>
#include<algorithm>

using namespace std;

int main(int argc, char const *argv[]){
    int a, b, c;
    
    cin >> a >> b >> c;
    
    if (a == b && b == c && a == c){
        cout << 10000 + a * 1000 << endl;
    } else if (a != b && b != c && a != c){
        cout << max(c, max(a, b)) * 100 << endl;
    } else {
        if (a == b) cout << 1000 + a * 100 << endl;
        else if (a == c) cout << 1000 + a * 100 << endl;
        else cout << 1000 + b * 100 << endl;
    }
}

