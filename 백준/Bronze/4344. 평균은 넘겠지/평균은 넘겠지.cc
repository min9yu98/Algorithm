#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <math.h>

using namespace std;

int main(int argc, char const *argv[]){
    ios_base::sync_with_stdio(false);    // C, C++ 동기화 해제
    cin.tie(NULL);    // 입력과 출력을 분리

    int c;
    cin >> c;
    
    for (int a = 0; a < c; a++){
        int n;
        double avg = 0, cnt = 0;
        int arr[1001] = {0, };

        cin >> n;
        for (int i = 0; i < n; i++){
            cin >> arr[i];
            avg += arr[i];
        }
        avg /= n;
        
        for (int i = 0; i < n; i++){
            if (avg < arr[i]) cnt++;
        }
        
        cout << fixed;
        cout.precision(3);
        cout << cnt / n * 100 * 1000 / 1000 << "%" << endl;
    }
}
