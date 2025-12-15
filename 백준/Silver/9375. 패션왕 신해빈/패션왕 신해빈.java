
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for (int tc = 0; tc < T; tc++) {
			Map<String, Integer> map = new HashMap<>();
			int n = Integer.parseInt(br.readLine());
			for (int k = 0; k < n; k++) {
				st = new StringTokenizer(br.readLine());
				st.nextToken();
				String category = st.nextToken();
				if (!map.containsKey((category))) {
					map.put(category, 1);
				} else {
					map.put(category, map.get(category) + 1);
				}
			}
			int result = 1;
			for (int value : map.values()) {
				result *= (value + 1);
			}
			System.out.println(result - 1);
		}
	}
}