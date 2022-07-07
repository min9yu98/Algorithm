#include <iostream>
#include<algorithm>

using namespace std;

int main(int argc, char const *argv[]){
    ios_base::sync_with_stdio(false);    // C, C++ 동기화 해제
    cin.tie(NULL);    // 입력과 출력을 분리
    
    int a, max = 0;
    int idx = 0;
    
    for (int i = 0; i < 9; i++){
        cin >> a;
        
        if (max < a){
            max = a;
            idx = i + 1;
        }
    }
    
    cout << max << endl << idx;
    
}
