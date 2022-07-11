#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <math.h>

using namespace std;

int d(int n){
    int sum = n;
    
    while(n != 0){
        sum += (n % 10);
        n /= 10;
    }
    
    return sum;
}

int main(int argc, char const *argv[]){
    ios_base::sync_with_stdio(false);    // C, C++ 동기화 해제
    cin.tie(NULL);    // 입력과 출력을 분리

    bool check[10001]{false};
    
    int n;
    for (int i = 1; i < 10001; i++){
        n = d(i);
        if (n < 10001) check[n] = true;
    }
    
    for (int i = 1; i < 10001; i++){
        if (!check[i]) cout << i << endl;
    }
}
