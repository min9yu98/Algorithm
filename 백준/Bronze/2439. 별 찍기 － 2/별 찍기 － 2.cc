#include <iostream>
#include<algorithm>

using namespace std;

int main(int argc, char const *argv[]){
    ios_base::sync_with_stdio(false);    // C, C++ 동기화 해제
    cin.tie(NULL);    // 입력과 출력을 분리
     
    int T;
    cin >> T;
    for(int i = 0; i < T; i++) {
        for (int k = T - i - 1; k > 0; k--) cout << " ";
        for (int j = 0; j <= i; j++) cout << "*";
        cout << endl;
    }
}

