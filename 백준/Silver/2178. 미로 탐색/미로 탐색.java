import java.io.*;
import java.util.*;

public class Main {

	static int[][] map;
	static boolean[][] visited;
	static int[][] dp;
	static int[] dx = {0, 0, 1, -1};
	static int[] dy = {1, -1, 0, 0};

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
		map = new int[n][m];
		visited = new boolean[n][m];
		dp = new int[n][m];

		for (int i = 0; i < n; i++) {
			String tmp = br.readLine();
			for (int j = 0; j < m; j++) {
				map[i][j] = tmp.charAt(j) - '0';
				dp[i][j] = 10001;
			}
		}

		Queue<int[]> q = new LinkedList<>();
		q.offer(new int[] {0, 0});
		dp[0][0] = 1;
		visited[0][0] = true;

		while (!q.isEmpty()) {
			int[] cur = q.poll();
			int x = cur[0], y = cur[1];
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i], ny = y + dy[i];
				if (0 <= nx && nx < n && 0 <= ny && ny < m) {
					if (map[nx][ny] == 1 && !visited[nx][ny]) {
						visited[nx][ny] = true;
						dp[nx][ny] = Math.min(dp[nx][ny], dp[x][y] + 1);
						q.offer(new int[] {nx, ny});
					}
				}
			}
		}

		bw.write(dp[n - 1][m - 1] + "\n");

		br.close();
		bw.flush();
		bw.close();
	}
}