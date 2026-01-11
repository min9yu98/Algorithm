
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int n;
	static int m;

	static int[][] arr;
	static boolean[][] visited;
	static int[][] res;
	static int[] dirX = {0, 0, 1, -1};
	static int[] dirY = {1, -1, 0, 0};

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		arr = new int[n][m];
		visited = new boolean[n][m];
		res = new int[n][m];

		int x = 0;
		int y = 0;
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				if (arr[i][j] == 2) {
					x = i;
					y = j;
				}
			}
		}

		bfs(x, y);

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (arr[i][j] == 1 && res[i][j] == 0 && !visited[i][j]) {
					System.out.print("-1 ");
					continue;
				}
				System.out.print(res[i][j] + " ");
			}
			System.out.println();
		}
	}

	private static void bfs(int x, int y) {
		Queue<int[]> queue = new LinkedList<>();
		queue.offer(new int[] {x, y});
		visited[x][y] = true;

		while (!queue.isEmpty()) {
			int[] coo = queue.poll();
			int a = coo[0];
			int b = coo[1];

			for (int i = 0; i < 4; i++) {
				int da = a + dirX[i];
				int db = b + dirY[i];
				if (da < n && db < m && da >= 0 && db >= 0) {
					if (!visited[da][db] && arr[da][db] == 1) {
						queue.offer(new int[] {da, db});
						visited[da][db] = true;
						res[da][db] = res[a][b] + 1;
					}
				}
			}
		}
	}
}