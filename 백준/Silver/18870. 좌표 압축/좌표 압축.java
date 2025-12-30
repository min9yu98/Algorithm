
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		List<Integer> list = new ArrayList<>();
		List<Integer> lst = new ArrayList<>();
		StringTokenizer st = new StringTokenizer(br.readLine());
		Map<Integer, Integer> map = new HashMap<>();
		for (int i = 0; i < N; i++) {
			int x = Integer.parseInt(st.nextToken());
			list.add(x);
			lst.add(x);
		}

		list.sort(Comparator.naturalOrder());

		int rank = 0;
		for (int i = 0; i < N; i++) {
			int x = list.get(i);
			if (!map.containsKey(x)) {
				map.put(x, rank);
				rank++;
			}
		}

		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < N; i++) {
			sb.append(map.get(lst.get(i)) + " ");
		}
		System.out.println(sb);
	}


}