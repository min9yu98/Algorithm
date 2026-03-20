import java.util.*;

class Solution {
    public String solution(String[] survey, int[] choices) {
        StringBuilder answer = new StringBuilder();
        Map<Character, Integer> map = getMap();
        
        for (int i = 0; i < survey.length; i++) {
            int score = choices[i];
            char sur1 = survey[i].charAt(0);
            char sur2 = survey[i].charAt(1);
            
            if (score >= 5) {
                switch (score) {
                    case 5: map.put(sur2, map.get(sur2) + 1); break;
                    case 6: map.put(sur2, map.get(sur2) + 2); break;
                    case 7: map.put(sur2, map.get(sur2) + 3); break;
                    default: break;
                }
            } else if (score <= 3) {
                switch (score) {
                    case 1: map.put(sur1, map.get(sur1) + 3); break;
                    case 2: map.put(sur1, map.get(sur1) + 2); break;
                    case 3: map.put(sur1, map.get(sur1) + 1); break;
                    default: break;
                }
            } else {
                continue;
            }
        }
        
        if (map.get('R') >= map.get('T')) answer.append('R');
        else answer.append('T');
        
        if (map.get('C') >= map.get('F')) answer.append('C');
        else answer.append('F');
        
        if (map.get('J') >= map.get('M')) answer.append('J');
        else answer.append('M');
        
        if (map.get('A') >= map.get('N')) answer.append('A');
        else answer.append('N');
        
        return answer.toString();
    }
    
    private Map<Character, Integer> getMap() {
        Map<Character, Integer> map = new HashMap<>();
        map.put('R', 0);
        map.put('T', 0);
        map.put('C', 0);
        map.put('F', 0);
        map.put('J', 0);
        map.put('M', 0);
        map.put('A', 0);
        map.put('N', 0);
        return map;
    }

}