//
//  hw3.cpp
//  Study
//
//  Created by 김민규 on 2022/09/13.
//

#include <stdio.h>
#include <set>
#include <algorithm>
#include <stdio.h>
#include <iostream>

using namespace std;

int main(){
    int n, k, num, min = 10001;
    int p[10001]; //p
    int p1[10001]; // p'
    int p2[10001] = {0, }; // p - p'
    
    set<int> s1; // p'
    set<int> s2; // p - p'
    
    cin >> n >> k;
    
    for (int i = 1; i < n + 1; i++){
        cin >> num;
        p[i] = num;
        s2.insert(num);
        p2[num]++;
    }
    
    int start = 1, end = 0;
    
    while(start <= n && end <= n){
        if (s1.size() >= s2.size()){
            if (s1.size() == s2.size() && s1.size() == k){
                if (min >= end - start + 1) min = end - start + 1;
            }
            start++;
            if (start > end) break;
            p1[p[start - 1]]--;
            if (p1[p[start - 1]] == 0) s1.erase(p[start - 1]);
            if (p2[p[start - 1]] == 0) s2.insert(p[start - 1]);
            p2[p[start - 1]]++;
        }
        else {
            end++;
            if (end > n) break;
            p2[p[end]]--;
            if (p2[p[end]] == 0) s2.erase(p[end]);
            if (p1[p[end]] == 0) s1.insert(p[end]);
            p1[p[end]]++;
        }
    }
    
    if (min == 10001) min = 0;
    cout << min << endl;
}
