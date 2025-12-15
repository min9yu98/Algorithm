
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int com = Integer.parseInt(br.readLine());
		int conn = Integer.parseInt(br.readLine());
		boolean[] visited = new boolean[com + 1];
		List<Integer>[] arr = new List[com + 1];
		for (int i = 0; i <= com; i++) arr[i] = new ArrayList<Integer>();

		for (int i = 1; i <= conn; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			arr[x].add(y);
			arr[y].add(x);
		}

		int result = 0;
		Queue<Integer> queue = new LinkedList<>();
		for (int i = 0; i < arr[1].size(); i++) {
			queue.offer(arr[1].get(i));
		}
		visited[1] = true;
		while (!queue.isEmpty()) {
			int now = queue.poll();
			if (!visited[now]) {
				visited[now] = true;
				for (int i = 0; i < arr[now].size(); i++) {
					queue.offer(arr[now].get(i));
				}
				result++;
			}
		}
		System.out.println(result);
	}
}