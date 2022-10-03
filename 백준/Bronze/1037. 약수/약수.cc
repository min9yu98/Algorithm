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

using namespace std;

int arr[51];
int maxi = 0;
int mini = 1000001;

int main(){
    int n, num;
    cin >> n;
    
    for (int i = 0; i < n; i++){
        cin >> num;
        if (num >= maxi) maxi = num;
        if (num <= mini) mini = num;
    }
    
    cout << mini * maxi << endl;
    
}
