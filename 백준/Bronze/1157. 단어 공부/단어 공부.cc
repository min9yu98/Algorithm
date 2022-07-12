#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <math.h>

using namespace std;

void ToLower( std::string & strBuf )
{
    std::transform( strBuf.begin(), strBuf.end(), strBuf.begin(), ::tolower );
}

int main(int argc, char const *argv[]){
    ios_base::sync_with_stdio(false);    // C, C++ 동기화 해제
    cin.tie(NULL);    // 입력과 출력을 분리
    
    int arr[26] = {0, };
    int max = 0;
    char ans = '?';
    
    string str;
    cin >> str;
    ToLower(str);
        
    for (int i = 0; i < str.length(); i++) arr[str[i] - '0' - 49]++;

    for (int i = 0; i < 26; i++){
        if (max < arr[i]) {
            max = arr[i];
            ans = i + 65;
        } else if (max == arr[i] && max != 0) ans = '?';
    }
    
    printf("%c\n", ans);
    
    
}
