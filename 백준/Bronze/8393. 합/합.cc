#include <iostream>
#include<algorithm>

using namespace std;

int main(int argc, char const *argv[]){
    int n, total = 0;
    cin >> n;
    
    for (int i = 1; i <= n; i++){
        total += i;
    }
    
    cout << total;
}

