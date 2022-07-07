#include <iostream>
#include<algorithm>

using namespace std;

int main(int argc, char const *argv[]){
    ios_base::sync_with_stdio(false);    // C, C++ 동기화 해제
    cin.tie(NULL);    // 입력과 출력을 분리
    
    int n;
    cin >> n;
    int arr[1000001];
    
    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }
    
    sort(arr, arr + n);
    
    cout << arr[0] << " " << arr[n - 1];
    
}
