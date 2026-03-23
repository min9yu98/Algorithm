import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        if (cacheSize == 0) {
            return cities.length * 5;
        }
        
        int answer = 0;

        ArrayList<String> arr = new ArrayList<>();
        for (String city : cities) {
            city = city.toUpperCase();
            if (!arr.contains(city)) {
                if (arr.size() >= cacheSize) {
                    arr.remove(0);
                }
                arr.add(city);
                answer += 5;
            } else {
                arr.remove(city);
                arr.add(city);
                answer += 1;
            }
        }
        
        return answer;
    }
}