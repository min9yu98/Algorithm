import java.util.*;

class Solution {
    public int solution(String message, int[][] spoiler_ranges) {
        int answer = 0;
        String[] msg = message.split(" ");
        int[] arr = new int[message.length()];
        int idx = 0;

        Map<String, Integer> map = new HashMap<>();
        Set<String> set = new HashSet<>();

        // 1. 문자 위치별 단어 인덱스 저장
        for (int i = 0; i < message.length(); i++) {
            if (message.charAt(i) == ' ') {
                arr[i] = -1;
                idx++;
            } else {
                arr[i] = idx;
            }
        }

        // 2. 스포일러에 포함된 단어 확인
        boolean[] isSpoiler = new boolean[msg.length];

        for (int i = 0; i < spoiler_ranges.length; i++) {
            int start = spoiler_ranges[i][0];
            int end = spoiler_ranges[i][1];

            for (int j = start; j <= end; j++) {
                if (arr[j] != -1) {
                    isSpoiler[arr[j]] = true;
                }
            }
        }

        // 3. 스포일러가 아닌 일반 단어 저장
        for (int i = 0; i < msg.length; i++) {
            if (!isSpoiler[i]) {
                map.put(msg[i],
                    map.getOrDefault(msg[i], 0) + 1);
            }
        }

        // 4. 중요한 단어 확인
        for (int i = 0; i < msg.length; i++) {
            if (isSpoiler[i]
                    && !map.containsKey(msg[i])
                    && !set.contains(msg[i])) {

                set.add(msg[i]);
                answer++;
            }
        }

        return answer;
    }
}