import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
		Map<String, Integer> map = new HashMap<>();

		int limit = 0;
		for (int i = 0; i < want.length; i++) {
			map.put(want[i], i);
			limit += number[i];
		}

		for (int i = 0; i < discount.length - limit + 1; i++) {
			int[] tmpArr = number.clone();
			for (int j = i; j < i + limit; j++) {
				if (map.containsKey(discount[j])) {
					int idx = map.get(discount[j]);
					tmpArr[idx]--;
					if (tmpArr[idx] < 0) break;
				} else {
					break;
				}
			}

			boolean flag = false;
			for (int j = 0; j < number.length; j++) {
				if (tmpArr[j] != 0) {
					flag = true;
					break;
				}
			}

			if (flag) continue;

			answer++;
		}

		return answer;
    }
}

// 치킨 사과 사과 바나나 쌀 사과 돼지고기 바나나 돼지고기 쌀 냄비 바나나 사과 바나나
// 1    1   
// 1        1