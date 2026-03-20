class Solution {
    public int solution(int n, int w, int num) {
        int[] arr = new int[n + 1];
        int answer = 0;
        int totalFloor = n / w + (n % w != 0 ? 1 : 0);
        int std = n - ((n / w) * w);
        
        if (n <= w) return 1;
        
        for (int i = n; i >= 1 + w; i--) {
            if (i % w == 0) {
                std = w;
            }
            
            arr[i - (2 * std - 1)] = arr[i] + 1;
            std--;
        }
        
        return arr[num] + 1;
    }
}

// 2n - 1
// 짝수 층 : 7 > 5 > 3 > 1
// 홀수 층 : 11, 9, 7, 5, 3, 1