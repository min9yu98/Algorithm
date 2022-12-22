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

string a, b, tmp, zero = "";
vector<int> av;
vector<int> bv;
vector<int> ans;

int main(){
    cin >> a >> b;
    
    if (b.length() > a.length()){
        tmp = a;
        a = b;
        b = tmp;
    }
    
    for (int i = 0; i < max(a.length(), b.length()) - min(a.length(), b.length()); i++){
        zero += "0";
    }
    
    b = zero + b;
            
    for (int i = a.length() - 1; i >= 0; i--){
        av.push_back(a[i] - '0');
    }
    
    for (int i = a.length() - 1; i >= 0; i--){
        bv.push_back(b[i] - '0');
    }

    int t = 0, one, ten = 0;
    for (int i = 0; i < a.length(); i++){
        t = av[i] + bv[i] + ten;
        one = t % 10;
        ten = t / 10;
        ans.push_back(one);
    }
    if (ten != 0) ans.push_back(ten);
    
    reverse(ans.begin(), ans.end());
    string ans2 = "";
    for (int i = 0; i < ans.size(); i++){
        ans2 += ans[i] + '0';
    }
    cout << ans2 << endl;
    return 0;
}