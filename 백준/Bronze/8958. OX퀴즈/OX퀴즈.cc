#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

vector<int> vec;

int ox(string str){
    int cum = 0;
    int cnt = 0;
    
    for (char &ch : str){
        if (ch == 'O'){
            cum++;
            cnt += cum;
        } else {
            cum = 0;
        }
    }
    
    return cnt;
}

int main(int argc, char const *argv[]){
    ios_base::sync_with_stdio(false);    // C, C++ 동기화 해제
    cin.tie(NULL);    // 입력과 출력을 분리

    int n;
    cin >> n;
    
    for (int i = 0; i < n; i++){
        string str;
        cin >> str;
        cout << ox(str) << endl;
    }
    
}
