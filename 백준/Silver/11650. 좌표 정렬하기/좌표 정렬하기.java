
import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		List<List<Integer>> arr = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			List<Integer> tmpArr = new ArrayList<>();
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			tmpArr.add(a);
			tmpArr.add(b);
			arr.add(tmpArr);
		}

		arr.sort((o1, o2) -> {
			if (o1.get(0).equals(o2.get(0))) {
				return o1.get(1) - o2.get(1);
			} else {
				return o1.get(0) - o2.get(0);
			}
		});
		StringBuilder sb = new StringBuilder();
		for (List<Integer> list : arr) {
			sb.append(list.get(0)).append(" ").append(list.get(1)).append("\n");
		}
		System.out.print(sb);
	}
}