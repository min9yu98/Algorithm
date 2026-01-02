
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int[][] arr;
	static boolean[] visited;
	static int N;
	static int M;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		arr = new int[N + 1][N + 1];
		visited = new boolean[N + 1];

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int u = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			arr[u][v] = 1;
			arr[v][u] = 1;
		}

		int cnt = 0;
		for (int i = 1; i <= N; i++) {
			if (!visited[i]) {
				bfs(i);
				cnt++;
			}
		}
		System.out.println(cnt);
	}

	private static void bfs(int x) {
		Queue<Integer> queue = new LinkedList<>();
		visited[x] = true;
		queue.offer(x);

		while (!queue.isEmpty()) {
			int n = queue.poll();

			for (int i = 1; i <= N; i++) {
				if (!visited[i] && arr[n][i] == 1) {
					queue.offer(i);
					visited[i] = true;
				}
			}
		}
	}
}