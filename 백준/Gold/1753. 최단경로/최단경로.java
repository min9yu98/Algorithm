
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.*;
import java.util.StringTokenizer;

public class Main {

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
		int V = Integer.parseInt(st.nextToken());
		int E = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(br.readLine());
		int[] numbers = new int[V + 1];
		boolean[] visited = new boolean[V + 1];
		ArrayList<ArrayList<Node>> graph = new ArrayList<>();
		for (int i = 0; i < V + 1; i++) {
			graph.add(new ArrayList<>());
		}

		for (int i = 0; i < E; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());

			graph.get(a).add(new Node(b, w));
		}

		for (int i = 1; i < V + 1;i ++) {
			numbers[i] = Integer.MAX_VALUE;
		}
		numbers[K] = 0;

		for (int i = 1; i < V + 1; i++) {
			int tmpIdx = 0;
			int tmpVal = Integer.MAX_VALUE;

			for (int j = 1; j < V + 1; j++) {
				if (!visited[j] && tmpVal > numbers[j]) {
					tmpIdx = j;
					tmpVal = numbers[j];
				}
			}

			visited[tmpIdx] = true;

			for (int j = 0; j < graph.get(tmpIdx).size(); j++) {
				Node tmpNode = graph.get(tmpIdx).get(j);

				if (numbers[tmpNode.idx] > numbers[tmpIdx] + tmpNode.weight) {
					numbers[tmpNode.idx] = numbers[tmpIdx] + tmpNode.weight;
				}
			}
		}

		for (int i = 1; i < V + 1; i++) {
			if (numbers[i] == Integer.MAX_VALUE) {
				System.out.println("INF");
			} else {
				System.out.println(numbers[i]);
			}
		}
	}
}