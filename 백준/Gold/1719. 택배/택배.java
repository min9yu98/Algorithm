
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.io.IOException;

public class Main {

	static int n;
	static int m;
	static List<Node>[] list;
	static int[][] result;

	static class Node {
		int idx;
		int weight;

		Node(int idx, int weight) {
			this.idx = idx;
			this.weight = weight;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		list = new List[n + 1];
		result = new int[n][n];

		for (int i = 1; i < n + 1; i++) {
			list[i] = new ArrayList<>();
		}

		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());

			list[a].add(new Node(b, c));
			list[b].add(new Node(a, c));
		}

		for (int i = 1; i < n + 1; i++) {
			dij(i);
		}

		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (i == j) {
					sb.append("- ");
					continue;
				}
				sb.append(result[i][j]).append(" ");
			}
			sb.append("\n");
		}

		System.out.println(sb.toString());
	}

	private static void dij(int start) {
		boolean[] visited = new boolean[n + 1];
		int[] min = new int[n + 1];

		for (int i = 1; i < n + 1; i++) {
			min[i] = Integer.MAX_VALUE;
		}

		PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> o1.weight - o2.weight);
		min[start] = 0;
		pq.offer(new Node(start, 0));

		while (!pq.isEmpty()) {
			Node now = pq.poll();

			if (min[now.idx] < now.weight) {
				continue;
			}

			if (!visited[now.idx]) {
				visited[now.idx] = true;
			}

			for (int i = 0; i < list[now.idx].size(); i++) {
				Node next = list[now.idx].get(i);

				if (!visited[next.idx] && now.weight + next.weight < min[next.idx]) {
					min[next.idx] = now.weight + next.weight;
					result[next.idx - 1][start - 1] = now.idx;
					pq.offer(new Node(next.idx, min[next.idx]));
				}
			}
		}
	}
}