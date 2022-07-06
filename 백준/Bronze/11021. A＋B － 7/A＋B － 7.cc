#include <iostream>
#include<algorithm>

using namespace std;

int main(int argc, char const *argv[]){
    ios_base::sync_with_stdio(false);    // C, C++ 동기화 해제
    cin.tie(NULL);    // 입력과 출력을 분리
     
    int T, a, b;
    cin >> T;
    for(int i = 0; i < T; i++) {
        cin >> a >> b;
        cout << "Case #" << i + 1 << ": " << a + b << endl;
    }
}

