
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.io.IOException;

public class Main {

	static int n, m;
	static List<Node>[] graph;

	static class Node implements Comparable<Node> {
		int idx;
		int weight;

		Node(int idx, int weight) {
			this.idx = idx;
			this.weight = weight;
		}

		@Override
		public int compareTo(Node node) {
			return this.weight - node.weight;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		n = Integer.parseInt(br.readLine());
		m = Integer.parseInt(br.readLine());

		graph = new List[n + 1];
		for (int i = 1; i < n + 1; i++) {
			graph[i] = new ArrayList<>();
		}

		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			int weight = Integer.parseInt(st.nextToken());

			graph[start].add(new Node(end, weight));
		}

		st = new StringTokenizer(br.readLine());
		int start = Integer.parseInt(st.nextToken());
		int end = Integer.parseInt(st.nextToken());

		dij(start, end);

	}

	private static void dij(int start, int end) {
		PriorityQueue<Node> queue = new PriorityQueue<>();
		int[] dist = new int[n + 1];
		int[] parent = new int[n + 1];

		Arrays.fill(dist, Integer.MAX_VALUE);

		dist[start] = 0;
		queue.offer(new Node(start, 0));

		while (!queue.isEmpty()) {
			Node nd = queue.poll();

			if (nd.weight > dist[nd.idx]) continue;

			for (Node next : graph[nd.idx]) {
				if (dist[next.idx] > dist[nd.idx] + next.weight) {
					dist[next.idx] = dist[nd.idx] + next.weight;
					parent[next.idx] = nd.idx;
					queue.offer(new Node(next.idx, dist[next.idx]));
				}
			}
		}

		List<Integer> path = new ArrayList<>();
		int cur = end;
		while (cur != 0) {
			path.add(cur);
			cur = parent[cur];
		}
		Collections.reverse(path);

		System.out.println(dist[end]);
		System.out.println(path.size());
		for (int city : path) {
			System.out.print(city + " ");
		}
	}

}