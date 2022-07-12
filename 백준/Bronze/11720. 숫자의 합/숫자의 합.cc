#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <math.h>

using namespace std;

int main(int argc, char const *argv[]){
    ios_base::sync_with_stdio(false);    // C, C++ 동기화 해제
    cin.tie(NULL);    // 입력과 출력을 분리
    
    int n, total = 0;
    string str;
    
    cin >> n >> str;
    
    for (int i = 0; i < n; i++){
        total += str[i] - '0';
    }
    
    cout << total << endl;
}
