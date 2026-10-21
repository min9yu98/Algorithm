class Solution {
    public int solution(int n, int k) {
        int bev = (int) n / 10;
        k = k - bev;
        return n * 12000 + (k > 0 ? k : 0) * 2000;
    }
}