
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

	static int[] visited;
	static int N;
	static int K;
	static int result = 0;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		visited = new int[100001];

		bfs(N);
		System.out.println(result);
	}

	private static void bfs(int start) {
		Queue<Integer> queue = new LinkedList<>();
		queue.offer(start);
		visited[start] = 1;

		while (!queue.isEmpty()) {
			int x = queue.poll();

			if (x == K) {
				result = visited[x] - 1;
				return;
			}
			if (x - 1 >= 0 && visited[x - 1] == 0) {
				queue.offer(x - 1);
				visited[x - 1] = visited[x] + 1;
			}
			if (x + 1 <= 100000 && visited[x + 1] == 0) {
				queue.offer(x + 1);
				visited[x + 1] = visited[x] + 1;
			}
			if (2 * x <= 100000 && visited[2 * x] == 0) {
				queue.offer(x * 2);
				visited[2 * x] = visited[x] + 1;
			}
		}
	}
}