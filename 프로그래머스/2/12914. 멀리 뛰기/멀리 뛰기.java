class Solution {
    public long solution(int n) {
        // n이 1이거나 2일 때는 배열을 만들 필요 없이 바로 정답을 반환
        if (n == 1) return 1;
        if (n == 2) return 2;
        
        // n이 3 이상일 때만 아래 로직 실행
        long[] arr = new long[n + 1];
        arr[1] = 1;
        arr[2] = 2;
        
        for (int i = 3; i <= n; i++) {
            arr[i] = (arr[i - 1] + arr[i - 2]) % 1234567;
        }
        
        return arr[n] % 1234567;
    }
}