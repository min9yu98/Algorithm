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
#include <map>

using namespace std;

int n, num, mini = 4001, maxi = -4001, maxi_cnt = 0, cnt = 0, most = -9999;
int arr[8001] = {0};
vector<int> v;
bool flag = false;
int mean, middle, range, most_val;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n;
    
    for (int i = 0; i < n; i++){
        cin >> num;
        mini = min(num, mini);
        maxi = max(num, maxi);
        cnt += num;
        v.push_back(num);
        arr[num + 4000]++;
    }
    
    sort(v.begin(), v.end());
    
    
    for (int i = 0; i <= 8000; i++){
        if (arr[i] == 0) continue;
        if (arr[i] == most){
            if (flag){
                most_val = i - 4000;
                flag = false;
            }
        }
        if (arr[i] > most){
            most = arr[i];
            most_val = i - 4000;
            flag = true;
        }
    }
    
   
    mean = round((float)cnt / n);
    middle = v[n / 2];
    range = maxi - mini;
    
    
    cout << mean << '\n' << middle << '\n' << most_val << '\n' << range << '\n';
    
    return 0;
}
