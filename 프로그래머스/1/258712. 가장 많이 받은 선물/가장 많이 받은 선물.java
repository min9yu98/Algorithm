import java.util.Map;
import java.util.HashMap;
import java.util.Collections;

class Solution {
	public int solution(String[] friends, String[] gifts) {
		Map<String, Map<String, Integer>> giftRecord = new HashMap<>();
		Map<String, Integer> giftScore = new HashMap<>();
		Map<String, Integer> nextMonthGiftScore = new HashMap<>();

		for (String friend: friends) {
			giftRecord.put(friend, new HashMap<>());
			giftScore.put(friend, 0);
			nextMonthGiftScore.put(friend, 0);
		}

		for (String gift : gifts) {
			String[] fr = gift.split(" ");
			String giver = fr[0];
			String receiver = fr[1];

			giftRecord.get(giver).put(receiver, giftRecord.get(giver).getOrDefault(receiver, 0) + 1);
			giftScore.put(giver, giftScore.get(giver) + 1);
			giftScore.put(receiver, giftScore.get(receiver) - 1);
		}

		for (String giver: friends) {
			for (String receiver: friends) {
				if (!giver.equals(receiver)) {
					int giverScore = giftRecord.get(giver).getOrDefault(receiver, 0);
					int receiverScore = giftRecord.get(receiver).getOrDefault(giver, 0);

					if (giverScore > receiverScore) {
						nextMonthGiftScore.put(giver, nextMonthGiftScore.get(giver) + 1);
					}
					if (giverScore == receiverScore && giftScore.get(giver) > giftScore.get(receiver)) {
						nextMonthGiftScore.put(giver, nextMonthGiftScore.get(giver) + 1);
					}
				}
			}
		}

		return Collections.max(nextMonthGiftScore.values());
	}
}