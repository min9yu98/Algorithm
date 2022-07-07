#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

vector<int> vec;

int main(int argc, char const *argv[]){
    ios_base::sync_with_stdio(false);    // C, C++ 동기화 해제
    cin.tie(NULL);    // 입력과 출력을 분리
    
    int arr[42] = {0, };
    int n, cnt = 0;
    
    for (int i = 0; i < 10; i++){
        cin >> n;
        arr[n % 42]++;
    }
    
    for (int i = 0; i < 42; i++){
        if (arr[i] != 0) cnt++;
    }
    
    cout << cnt;
    
}
