class Solution {    
    public int solution(int number, int limit, int power) {
        int result = 0;
        for (int i = 1; i < number + 1; i++) {
            result += fac(i, limit, power);
        }
        return result;
    }
    
    private int fac(int x, int lim, int power) {
        int cnt = 0;
        for (int i = 1; i * i <= x; i++) {
            if (x % i == 0) {
                cnt++;
                
                if (i != x / i) {
                    cnt++;
                }
            }
        }
        if (cnt > lim) {
            return power;
        }
        return cnt;
    }
}