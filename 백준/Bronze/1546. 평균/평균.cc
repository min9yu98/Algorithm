#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

vector<int> vec;

int main(int argc, char const *argv[]){
    ios_base::sync_with_stdio(false);    // C, C++ 동기화 해제
    cin.tie(NULL);    // 입력과 출력을 분리

    double n, arr[1001], max = 0;
    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> arr[i];
        if (max < arr[i]) max = arr[i];
    }
    
    double sum = 0;
    for (int i = 0; i < n; i++){
        sum += (arr[i] / max) * 100;
    }
    
    cout << sum / n;
    
}
