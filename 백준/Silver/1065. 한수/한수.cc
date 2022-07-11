#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <math.h>

using namespace std;

int han(int n){
    int first, second, cnt = 0;
    if (n < 100) cnt = n;
    else{
        for(int i = 100; i <= n; i++){
            first = (i / 100) - ((i % 100) / 10);
            second = ((i % 100) / 10) - (i % 10);
            
            if (first == second) cnt++;
        }
        cnt += 99;
    }
    
    return cnt;
}

int main(int argc, char const *argv[]){
    ios_base::sync_with_stdio(false);    // C, C++ 동기화 해제
    cin.tie(NULL);    // 입력과 출력을 분리
    
    int n;
    cin >> n;
    
    cout << han(n) << endl;
}
