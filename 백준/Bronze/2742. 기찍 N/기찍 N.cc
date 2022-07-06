#include <iostream>
#include<algorithm>

using namespace std;

int main(int argc, char const *argv[]){
    ios_base::sync_with_stdio(false);    // C, C++ 동기화 해제
    cin.tie(NULL);    // 입력과 출력을 분리
     
    int T;
    cin >> T;
    for(int i = T; i >= 1; i--) {
        cout << i << "\n"; // endl 대신 \n 을 쓰기
    }
}

