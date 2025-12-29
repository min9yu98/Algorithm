
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

	static boolean[] visitedBfs;
	static boolean[] visitedDfs;
	static List<Integer>[] node;
	static int N;
	static int M;
	static int V;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		V = Integer.parseInt(st.nextToken());

		node = new ArrayList[N + 1];
		visitedBfs = new boolean[N + 1];
		visitedDfs = new boolean[N + 1];
		for (int i = 0; i < N + 1; i++) {
			node[i] = new ArrayList<>();
		}

		for (int o = 0; o < M; o++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			node[x].add(y);
			node[y].add(x);
		}

		for (int i = 0; i < N + 1; i++) {
			node[i].sort(Integer::compareTo);
		}

		dfs(V);
		System.out.println();
		bfs();
	}

	public static void bfs() {
		Queue<Integer> q = new LinkedList<>();
		q.offer(V);
		visitedBfs[V] = true;
		System.out.print(V + " ");

		while (!q.isEmpty()) {
			int x = q.poll();
			for (int i = 0; i < node[x].size(); i++) {
				int a = node[x].get(i);
				if (!visitedBfs[a]) {
					q.offer(a);
					visitedBfs[a] = true;
					System.out.print(a + " ");
				}
			}
		}
	}

	public static void dfs(int n) {
		if (visitedDfs[n]) return;

		System.out.print(n + " ");
		visitedDfs[n] = true;
		for (int i = 0; i < node[n].size(); i++) {
			int x = node[n].get(i);
			if (!visitedDfs[x]) {
				dfs(x);
			}
		}
	}

}