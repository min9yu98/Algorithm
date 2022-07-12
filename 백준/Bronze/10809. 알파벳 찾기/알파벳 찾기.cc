#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <math.h>

using namespace std;

int main(int argc, char const *argv[]){
    ios_base::sync_with_stdio(false);    // C, C++ 동기화 해제
    cin.tie(NULL);    // 입력과 출력을 분리
    
    string str;
    cin >> str;
    
    string alpha = "abcdefghijklmnopqrstuvwxyz";
    
    for (int i = 0; i < alpha.length(); i++){
        cout << (int)str.find(alpha[i]) << " ";
    }
}
