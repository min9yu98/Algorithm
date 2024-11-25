import java.io.*;
import java.util.*;

public class Main {

	static int[] dx = {-1, 0, 1, 0};
	static int[] dy = {0, 1, 0, -1};
	static int[][] map;
	static boolean[][] visit;

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
		Queue<int[]> q = new LinkedList<>();

		map = new int[n][m];
		visit = new boolean[n][m];

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		int max = 0;
		int num = 0;

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j] == 0 || visit[i][j]) continue;
				num++;
				visit[i][j] = true;
				q.offer(new int[] {i, j});
				int area = 0;
				while (!q.isEmpty()) {
					area++;
					int[] temp = q.poll();
					int x = temp[0], y = temp[1];

					for (int dir = 0; dir < 4; dir++) {
						int nx = x + dx[dir], ny = y + dy[dir];
						if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
							if (!visit[nx][ny] && map[nx][ny] == 1) {
								visit[nx][ny] = true;
								q.offer(new int[]{nx, ny});
							}
						}
					}
				}
				max = Math.max(max, area);
			}
		}

		System.out.println(num);
		System.out.println(max);
	}
}