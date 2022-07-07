#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main(int argc, char const *argv[]){
    ios_base::sync_with_stdio(false);    // C, C++ 동기화 해제
    cin.tie(NULL);    // 입력과 출력을 분리
    
    int a, b, c, n;
    int arr[10] = {0, };
    cin >> a >> b >> c;
    
    n = a * b * c;
    
    string num = to_string(n);
    
    for (int i = 0; i < num.length(); i++){
        int c = num[i] - '0';
        arr[c]++;
    }
    
    for (int i = 0; i < 10; i++) cout << arr[i] << endl;
    
}
