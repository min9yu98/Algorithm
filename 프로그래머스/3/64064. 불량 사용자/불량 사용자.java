import java.util.*;

class Solution {
    public int solution(String[] user_id, String[] banned_id) {
        Set<Integer> set = new HashSet<>();
        int[] arr = new int[banned_id.length];
        for (int i = 0; i < banned_id.length; i++) {
            int e = 0;
            for (int j = 0; j < user_id.length; j++) {
                if (banned_id[i].length() != user_id[j].length()) {
                    continue;
                }
                
                boolean check = true;
                for (int k = 0; k < user_id[j].length(); k++) {
                    if (banned_id[i].charAt(k) == '*') continue;
                    if (user_id[j].charAt(k) != banned_id[i].charAt(k)) {
                        check = false;
                        break;
                    }
                }
                
                if (check) {
                    e |= 1 << j;
                }
            }
            
            arr[i] = e;
        }
        
        dfs(0, 0, arr, user_id.length, set);
        
        return set.size();
    }
    
    private void dfs(int depth, int mask, int[] possible, int n, Set<Integer> s) {
        if (depth == possible.length) {
            s.add(mask);
            return;
        }
        
        for (int i = 0; i < n; i++) {
            int bit = 1 << i;
            
            if ((possible[depth] & bit) == 0) continue;
            
            if ((mask & bit) != 0) continue;
            
            dfs(depth + 1, mask | bit, possible, n, s);
        }
    }
}

// 11000 00010
// 10100 10100 00011
// 11000 10100 00011 00011