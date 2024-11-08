import java.util.Map;
import java.util.HashMap;

class Solution {
	public String solution(String[] participants, String[] completions) {
		String answer = "";
		Map<String, Integer> record = new HashMap<>();
		for (String participant: participants) {
			record.put(participant, record.getOrDefault(participant, 0) + 1);
		}
		for (String completion: completions) {
			record.put(completion, record.get(completion) - 1);
		}
		for (String participant: participants) {
			if (record.get(participant) == 1) {
				return participant;
			}
		}
		return answer;
	}
}