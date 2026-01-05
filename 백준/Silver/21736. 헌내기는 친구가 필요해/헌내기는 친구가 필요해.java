
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static String[][] board;
	static boolean[][] visited;
	static int N;
	static int M;
	static int result = 0;
	static int[][] dir = new int[][] {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		board = new String[N][M];
		visited = new boolean[N][M];
		int x = -1, y = -1;
		for (int i = 0; i < N; i++) {
			String str = br.readLine();
			for (int j = 0; j < M; j++) {
				board[i][j] = String.valueOf(str.charAt(j));
				if ("I".equals(board[i][j])) {
					x = i;
					y = j;
				}
			}
		}

		bfs(x, y);
		System.out.println(result > 0 ? result : "TT");
	}

	private static void bfs(int x, int y) {
		Queue<int[]> queue = new LinkedList<>();
		queue.offer(new int[] {x, y});
		visited[x][y] = true;

		while (!queue.isEmpty()) {
			int[] tmpA = queue.poll();
			int a = tmpA[0];
			int b = tmpA[1];

			for (int i = 0; i < 4; i++) {
				int da = a + dir[i][0];
				int db = b + dir[i][1];
				if (da < 0 || da >= N || db < 0 || db >= M) continue;
				if (!visited[da][db] && !"X".equals(board[da][db])) {
					if ("P".equals(board[da][db])) {
						result++;
					}
					visited[da][db] = true;
					queue.offer(new int[] {da, db});
				}
			}
		}
	}

}