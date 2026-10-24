class Solution {
    public int solution(int[] info, int[][] edges) {
        int answer = 1;
        int n = info.length;
        
        int[] children = new int[n];
        
        for (int[] edge : edges) {
            int start = edge[0];
            int end = edge[1];
            children[start] |= 1 << end;
        }
        
        boolean[] dp = new boolean[1 << n];
        dp[1] = true;
        
        for (int mask = 0; mask < (1 << n); mask++) {
            if (!dp[mask]) continue;
            
            int sheep = 0;
            int wolf = 0;
            int available = 0;
            
            for (int i = 0; i < n; i++) {
                int bit = 1 << i;
                
                if ((mask & bit) == 0) continue;
                
                if (info[i] == 0) {
                    sheep++;
                } else {
                    wolf++;
                }
                
                available |= children[i];
            }
            
            answer = Math.max(answer, sheep);
            
            available &= ~mask;
            
            for (int i = 0; i < n; i++) {
                int bit = 1 << i;

                if ((available & bit) == 0) continue;

                int nextSheep = sheep;
                int nextWolf = wolf;

                if (info[i] == 0) {
                    nextSheep++;
                } else {
                    nextWolf++;
                }

                if (nextSheep > nextWolf) {
                    int nextMask = mask | bit;
                    dp[nextMask] = true;
                }
            }
        }
        
        return answer;
    }
}
