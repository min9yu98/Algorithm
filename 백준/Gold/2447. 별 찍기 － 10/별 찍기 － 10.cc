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

#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
using namespace std;

int n;

void star(int i, int j, int n){
    if ((i / n) % 3 == 1 && (j / n) % 3 == 1){
        cout << " ";
    } else {
        if (n / 3 == 0){
            cout << "*";
        } else {
            star(i, j, n / 3);
        }
    }
}

int main(){
    fastio;

    cin >> n;

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            star(i, j, n);
        }
        cout << '\n';
    }

    return 0;
}
