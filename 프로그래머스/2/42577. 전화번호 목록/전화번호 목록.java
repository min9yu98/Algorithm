import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        if (phone_book.length == 1) return true;
                
        HashMap<String, Boolean> map = new HashMap<>();
        for (String phone : phone_book) {
            map.putIfAbsent(phone, true);
        }
        
        for (int i = 0; i < phone_book.length; i++) {
            if (phone_book[i].length() == 1) continue;
            for (int j = 1; j < phone_book[i].length(); j++) {
                if (map.getOrDefault(phone_book[i].substring(0, j), false)) {
                    return false;
                }
            }
        }
        return true;
    }
}