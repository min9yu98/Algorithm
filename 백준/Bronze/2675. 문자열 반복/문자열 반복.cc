#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <math.h>

using namespace std;

int main(int argc, char const *argv[]){
    ios_base::sync_with_stdio(false);    // C, C++ 동기화 해제
    cin.tie(NULL);    // 입력과 출력을 분리
    
    int n, k;
    string str;
    cin >> n;
    
    for (int i = 0; i < n; i++){
        cin >> k >> str;
        
        for (int j = 0; j < str.length(); j++){
            for (int m = 0; m < k; m++) cout << str[j];
        }
        cout << endl;
    }
}
