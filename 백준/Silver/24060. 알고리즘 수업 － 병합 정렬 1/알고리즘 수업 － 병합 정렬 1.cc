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

int* A;
int n, cnt = 0, k;

void merge(int* A, int start, int mid, int end, int k){
    int tmp[end + 2];
    int i = start, j = mid + 1, t = 1;

    while (i <= mid && j <= end){
        if (A[i] <= A[j]){
            tmp[t++] = A[i++];
        } else {
            tmp[t++] = A[j++];
        }
    }
    while (i <= mid) tmp[t++] = A[i++];
    while (j <= end) tmp[t++] = A[j++];

    i = start;
    t = 1;
    while (i <= end){
        A[i++] = tmp[t++];
        if (++cnt == k) cout << tmp[t - 1] << '\n';
    }
}

void merge_sort(int* A, int start, int end, int k){
    int mid;
    if (start < end){
        mid = (start + end) / 2;
        merge_sort(A, start, mid, k);
        merge_sort(A, mid + 1, end, k);
        merge(A, start, mid, end, k);
    }
}

int main(){
    fastio;

    cin >> n >> k;

    A = new int[n];
    for (int i = 0; i < n; i++){
        cin >> A[i];
    }

    merge_sort(A, 0, n - 1, k);

    if (cnt < k) cout << -1 << '\n';

    return 0;
}
