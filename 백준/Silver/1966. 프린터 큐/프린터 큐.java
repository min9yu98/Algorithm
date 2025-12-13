
import java.io.*;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for (int i = 0; i < T; i++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			st = new StringTokenizer(br.readLine());
			LinkedList<int[]> q = new LinkedList<>();
			for (int j = 0; j < N; j++) {
				q.offer(new int[] {j, Integer.parseInt(st.nextToken())});
			}

			int cnt = 0;

			while (!q.isEmpty()) {
				int[] front = q.poll();
				boolean isMax = true;

				for (int j = 0; j < q.size(); j++) {
					if (front[1] < q.get(j)[1]) {
						q.offer(front);
						for (int k = 0; k < j; k++) {
							q.offer(q.poll());
						}
						isMax = false;
						break;
					}
				}
				if (!isMax) {
					continue;
				}
				cnt++;
				if (front[0] == M) {
					break;
				}
			}
			System.out.println(cnt);
		}
	}

}