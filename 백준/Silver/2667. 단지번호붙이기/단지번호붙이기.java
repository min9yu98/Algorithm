
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int N;
	static int[][] board;
	static boolean[][] visited;

	static int total = 0;
	static List<Integer> result = new ArrayList<>();
	static int[][] dir = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		board = new int[N][N];
		visited = new boolean[N][N];
		for (int i = 0; i < N; i++) {
			String line = br.readLine();
			for (int j = 0; j < N; j++) {
				board[i][j] = line.charAt(j) - '0';
			}
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (!visited[i][j] && board[i][j] == 1) {
					bfs(i, j);
					total++;
				}
			}
		}

		System.out.println(total);
		result.sort(Comparator.naturalOrder());
		for (int cnt : result) {
			System.out.println(cnt);
		}
	}

	private static void bfs(int x, int y) {
		Queue<int[]> queue = new LinkedList<>();
		queue.offer(new int[] {x, y});
		visited[x][y] = true;
		int tmpCnt = 1;

		while (!queue.isEmpty()) {
			int[] tmp = queue.poll();
			int a = tmp[0];
			int b = tmp[1];

			for (int i = 0; i < 4; i++) {
				int da = a + dir[i][0];
				int db = b + dir[i][1];
				if ((da >= 0 && da < N) && (db >= 0 && db < N)) {
					if (!visited[da][db] && board[da][db] == 1) {
						queue.offer(new int[] {da, db});
						visited[da][db] = true;
						tmpCnt++;
					}
				}
			}
		}

		result.add(tmpCnt);
	}
}