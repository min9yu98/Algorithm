import java.io.*;
import java.util.*;

public class Main {

	static int[][] map;
	static boolean[][] visited;
	static int[][] cnt;
	static int[] dx = {0, 0, 1, -1};
	static int[] dy = {1, -1, 0, 0};

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
		map = new int[m][n];
		visited = new boolean[m][n];
		cnt = new int[m][n];

		int total = 0; // 채우고 있는 갯수
		int check = 0; // 채워지는 갯수
		Queue<int[]> q = new LinkedList<>();
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				if (map[i][j] == 1) {
					q.offer(new int[] {i, j});
					visited[i][j] = true;
				}
				if (map[i][j] == 0) {
					check++;
				}
				cnt[i][j] = 0;
			}
		}

		while (!q.isEmpty()) {
			int[] tmp = q.poll();
			int x = tmp[0], y = tmp[1];

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i], ny = y + dy[i];
				if (0 <= nx && nx < m && 0 <= ny && ny < n) {
					if (!visited[nx][ny] && map[nx][ny] == 0) {
						visited[nx][ny] = true;
						map[nx][ny] = 1;
						total++;
						cnt[nx][ny] = cnt[x][y] + 1;
						q.offer(new int[] {nx, ny});
					}
				}
			}
		}

		if (total == check) {
			int max = 0;
			for (int i = 0; i < m; i++) {
				for (int j = 0; j < n; j++) {
					max = Math.max(max, cnt[i][j]);
				}
			}
			System.out.println(max);
		} else {
			System.out.println(-1);
		}
	}
}