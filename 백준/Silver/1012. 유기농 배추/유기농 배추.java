
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int[][] ground;
	static boolean[][] check;
	static int weight;
	static int height;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for (int o = 0; o < T; o++) {
			st = new StringTokenizer(br.readLine());
			weight = Integer.parseInt(st.nextToken());
			height = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());

			ground = new int[weight][height];
			check = new boolean[weight][height];

			for (int i = 0; i < K; i++) {
				st = new StringTokenizer(br.readLine());
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				ground[x][y] = 1;
			}

			int cnt = 0;

			for (int i = 0; i < weight; i++) {
				for (int j = 0; j < height; j++) {
					if (ground[i][j] == 1 && !check[i][j]) {
						bfs(i, j);
						cnt++;
					}
				}
			}
			System.out.println(cnt);
		}
	}

	public static void bfs(int startX, int startY) {
		Queue<int[]> q = new LinkedList<>();
		q.offer(new int[] {startX, startY});
		check[startX][startY] = true;

		int[] mx = {0, 0, 1, -1};
		int[] my = {1, -1, 0, 0};

		while (!q.isEmpty()) {
			int[] poll = q.poll();

			for (int i = 0; i < 4; i++) {
				int dx = poll[0] + mx[i];
				int dy = poll[1] + my[i];

				if (dx < 0 || dx >= weight || dy < 0 || dy >= height) {
					continue;
				}

				if (ground[dx][dy] == 1 && !check[dx][dy]) {
					q.offer(new int[] {dx, dy});
					check[dx][dy] = true;
				}
			}
		}
	}
}