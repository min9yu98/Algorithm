#include <iostream>
#include<algorithm>

using namespace std;

int main(int argc, char const *argv[]){
    ios_base::sync_with_stdio(false);    // C, C++ 동기화 해제
    cin.tie(NULL);    // 입력과 출력을 분리
    
    int n, end, tmp = 0;
    int cnt = 0;
    cin >> n;
    end = n;
    
    if (n == tmp){
        cout << 1 << endl;
        return 0;
    }
    
    while(tmp != end) {

        tmp = (n / 10) + (n % 10);
        cnt += 1;
        tmp = (tmp % 10) + ((n % 10) * 10);
        
        n = tmp;
    }
    
    cout << cnt << endl;
}
