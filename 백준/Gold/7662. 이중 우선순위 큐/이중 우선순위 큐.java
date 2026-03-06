
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;
import java.util.TreeMap;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for (int tc = 0; tc < T; tc++) {
			TreeMap<Integer, Integer> tm = new TreeMap<>();
			int k = Integer.parseInt(br.readLine());
			for (int i = 0; i < k; i++) {
				st = new StringTokenizer(br.readLine());

				String cmd = st.nextToken();
				int num = Integer.parseInt(st.nextToken());

				if ("I".equals(cmd)) {
					tm.put(num, tm.getOrDefault(num, 0) + 1);
				} else {
					int n;
					if (tm.isEmpty()) continue;
					if (num == 1) {
						n = tm.lastKey();
					} else {
						n = tm.firstKey();
					}
					if (tm.put(n, tm.get(n) - 1) == 1) {
						tm.remove(n);
					}
				}
			}

			if (tm.isEmpty()) {
				System.out.println("EMPTY");
			} else {
				System.out.println(tm.lastKey() + " " + tm.firstKey());
			}
		}
	}

}