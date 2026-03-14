import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        boolean c = false;
        
        StringBuilder sb = new StringBuilder();
        sb.append(s);
        c = check(sb.toString());
        if (c) answer++;
        for (int i = 0; i < s.length() - 1; i++) {
            sb.append(sb.charAt(0));
            sb.deleteCharAt(0);
            c = check(sb.toString());
            if (c) answer++;
        }
        
         return answer;
    }
    
    public boolean check(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            if (stack.isEmpty()) {
                stack.add(s.charAt(i));
                continue;
            }
            
            if ('(' == s.charAt(i) || '{' == s.charAt(i) || '[' == s.charAt(i)) {
                stack.add(s.charAt(i));
            } else {
                if (stack.isEmpty()) continue;
                
                if (')' == s.charAt(i)) {
                    if (stack.peek() == '(') stack.pop();
                } else if ('}' == s.charAt(i)) {
                    if (stack.peek() == '{') stack.pop();
                } else if (']' == s.charAt(i)) {
                    if (stack.peek() == '[') stack.pop();
                }
            }
        }
        
        return stack.isEmpty();
    }
}