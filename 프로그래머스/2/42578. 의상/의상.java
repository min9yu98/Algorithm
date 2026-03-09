import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        
        Map<String, Integer> m = new HashMap<>();
        for (String[] cloth: clothes) {
            m.put(cloth[1], m.getOrDefault(cloth[1], 1) + 1);
        }
        
        for (int i: m.values()) {
            answer *= i;
        }
        
        return answer - 1;
    }
}