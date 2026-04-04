
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.io.IOException;

class Node implements Comparable<Node> {
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

public class Main {

	static int n;
	static int m;
	static List<Node>[] arr;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		n = Integer.parseInt(br.readLine());
		m = Integer.parseInt(br.readLine());

		arr = new List[n + 1];
		for (int i = 0; i < n + 1; i++) {
			arr[i] = new ArrayList<>();
		}

		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());

			arr[a].add(new Node(b, c));
		}

		st = new StringTokenizer(br.readLine());
		int start = Integer.parseInt(st.nextToken());
		int end = Integer.parseInt(st.nextToken());

		dij(start, end);
	}

	public static void dij(int start, int end) {
		PriorityQueue<Node> pq = new PriorityQueue<>();
		int[] min = new int[n + 1];
		int[] parentIdx = new int[n + 1];

		for (int i = 1; i < n + 1; i++) {
			min[i] = Integer.MAX_VALUE;
		}

		min[start] = 0;
		pq.offer(new Node(start, 0));

		while (!pq.isEmpty()) {
			Node now = pq.poll();

			if (now.weight > min[now.idx]) continue;
			
			for (int i = 0; i < arr[now.idx].size(); i++) {
				Node next = arr[now.idx].get(i);
				
				if (now.weight + next.weight < min[next.idx]) {
					min[next.idx] = now.weight + next.weight;
					pq.offer(new Node(next.idx, min[next.idx]));
					parentIdx[next.idx] = now.idx;
				}
			}
		}

		System.out.println(min[end]);

		List<Integer> path = new ArrayList<>();
		int cur = end;
		while (cur != 0) {
			path.add(cur);
			cur = parentIdx[cur];
		}
		Collections.reverse(path);
		System.out.println(path.size());
		for (int city : path) {
			System.out.print(city + " ");
		}

	}

}