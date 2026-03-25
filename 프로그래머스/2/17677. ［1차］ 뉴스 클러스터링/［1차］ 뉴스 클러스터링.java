import java.util.*;

class Solution {
    public int solution(String str1, String str2) {
        ArrayList<String> arr1 = new ArrayList<>();
        ArrayList<String> arr2 = new ArrayList<>();
        
        for (int i = 0; i < str1.length() - 1; i++) {
            String s = str1.substring(i, i + 2);
            if (s.matches("[a-zA-Z]{2}")) {
                arr1.add(s.toLowerCase());
            }
        }
        
        for (int i = 0; i < str2.length() - 1; i++) {
            String s = str2.substring(i, i + 2);
            if (s.matches("[a-zA-Z]{2}")) {
                arr2.add(s.toLowerCase());
            }
        }
        
        ArrayList<String> temp = new ArrayList<>(arr2);
        double same = 0;
        for (String str : arr1) {
            if (temp.contains(str)) {
                same++;
                temp.remove(str);
            }
        }
        
        double answer = arr1.size() + arr2.size() - same;
        if (answer == 0) return 65536;
        
        return (int)(same / answer * 65536);
    }
}