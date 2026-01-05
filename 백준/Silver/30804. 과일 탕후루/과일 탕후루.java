
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[] tanghuru = new int[N];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			tanghuru[i] = Integer.parseInt(st.nextToken());
		}

		HashMap<Integer, Integer> cnt = new HashMap<>();
		int maxLen = 0;
		int left = 0;

		for (int i = 0; i < N; i++) {
			cnt.put(tanghuru[i], cnt.getOrDefault(tanghuru[i], 0) + 1);

			while (cnt.size() > 2) {
				cnt.put(tanghuru[left], cnt.get(tanghuru[left]) - 1);
				if (cnt.get(tanghuru[left]) == 0) {
					cnt.remove(tanghuru[left]);
				}
				left++;
			}

			maxLen = Math.max(maxLen, i - left + 1);
		}

		System.out.println(maxLen);
	}
}