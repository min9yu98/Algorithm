import java.util.*;

class Solution {
    public int solution(String message, int[][] spoiler_ranges) {
        int answer = 0;
        String[] msg = message.split(" ");
        int[] arr = new int[message.length()];
        boolean[] spoil = new boolean[msg.length];
        
        Map<String, Integer> map = new HashMap<>();
        Set<String> set = new HashSet<>();
        
        int idx = 0;
        for (int i = 0; i < message.length(); i++) {
            if (message.charAt(i) == ' ') {
                arr[i] = -1;
                idx++;
            } else {
                arr[i] = idx;
            }
        }
        
        for (int i = 0; i < spoiler_ranges.length; i++) {
            int start = spoiler_ranges[i][0];
            int end = spoiler_ranges[i][1];
            
            for (int j = start; j <= end; j++) {
                if (arr[j] != -1) {
                    spoil[arr[j]] = true;
                }
            }
        }
        
        for (int i = 0; i < msg.length; i++) {
            if (!spoil[i]) {
                map.put(msg[i], map.getOrDefault(msg[i], 0) + 1);
            }
        }
        
        for (int i = 0; i < msg.length; i++) {
            if (spoil[i] && !map.containsKey(msg[i]) && !set.contains(msg[i])) {
                answer++;
                set.add(msg[i]);
            }
        }
        
        return answer;
    }
}