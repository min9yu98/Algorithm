class Solution {
    public int solution(int[][] signals) {
        int limit = 1;
        for (int[] signal : signals) {
            int sum = signal[0] + signal[1] + signal[2];
            limit = lcd(limit, sum);
        }
        
        for (int time = 1; time <= limit; time++) {
            boolean check = true;
            
            for (int[] signal : signals) {
                int green = signal[0];
                int yellow = signal[1];
                int red = signal[2];
                
                int cycle = green + yellow + red;
                int point = (time - 1) % cycle;
                
                if (point < green || point >= green + yellow) {
                    check = false;
                    break;
                }
            }
            
            if (check) {
                return time;
            }
        }
        
        return -1;
    }
    
    private int gcd(int a, int b) {
        while (b != 0) {
            int tmp = b;
            b = a % b;
            a = tmp;
        }
        
        return a;
    }
    
    private int lcd(int a, int b) {
        return a / gcd(a, b) * b;
    }
}