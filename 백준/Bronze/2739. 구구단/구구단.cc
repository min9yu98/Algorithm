#include <iostream>
#include<algorithm>

using namespace std;

int main(int argc, char const *argv[]){
    int n;
    cin >> n;
    
    for (int i = 1; i < 10; i++){
        cout << n << " * " << i << " = " << n * i << endl;
    }
}

