#include <stdio.h>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <ostream>
#include <string>
#include <cstring>
#include <sstream>
#include <time.h>
#include <queue>
#include <cstdlib>
#include <stdbool.h>

using namespace std;

int n;
bool asc[123] = {false, };
bool sub_asc[123] = {false, };
bool checking = true;
int cnt = 0;

int main(){
    cin >> n;
    string str;
    
    for (int i = 0; i < n; i++){
        cin >> str;
        
        for (int j = 0; j < str.length() - 1; j++){
            if (asc[str[j]]) {
                checking = false;
                break;
            }
            else if (!asc[str[j]]){
                if (str[j] != str[j + 1]) asc[(int)str[j]] = true;
            }
        }
        if (asc[str[str.length() - 1]]){
            checking = false;
        }
        if (checking){
            cnt++;
        } else {
            checking = true;
        }
        copy(&sub_asc[0], &sub_asc[0] + 123, &asc[0]);
    }
    
    cout << cnt << endl;
    
    return 0;
}
