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

int n;
vector<pair<int, int>> vp;

void hanoi(int num, int start, int path, int end){
    if (num == 1){
        vp.push_back(pair<int, int> (start, end));
        return ;
    }
    hanoi(num - 1, start, end, path);
    vp.push_back(pair<int, int> (start, end));
    hanoi(num - 1, path, start, end);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n;
    
    hanoi(n, 1, 2, 3);
    cout << vp.size() << endl;
    for (int i = 0; i < vp.size(); i++){
        cout << vp[i].first << " " << vp[i].second << '\n';
    }
    
    return 0;
}
