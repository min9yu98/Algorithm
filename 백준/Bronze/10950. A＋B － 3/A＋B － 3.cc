#include <iostream>
#include<algorithm>

using namespace std;

int main(int argc, char const *argv[]){
    int n, x, y;
    cin >> n;
    
    
    for (int i = 0; i < n; i++){
        cin >> x >> y;
        cout << x + y << endl;
    }
}

