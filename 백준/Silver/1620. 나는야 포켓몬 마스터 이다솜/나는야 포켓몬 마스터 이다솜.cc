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

map<string, string> m;
map<string, string> m2;
int N, M;
string str;

int main(){
    fastio;

    cin >> N >> M;

    for (int i = 1; i <= N; i++){
        cin >> str;
        m.insert(make_pair(str, to_string(i)));
        m2.insert(make_pair(to_string(i), str));
    }

    for (int i = 0; i < M; i++){
        cin >> str;

        if (str[0] >= 65 && str[0] <= 90){
            cout << m[str] << '\n';
        } else {
            cout << m2[str] << '\n';
        }

    }
    return 0;
}
