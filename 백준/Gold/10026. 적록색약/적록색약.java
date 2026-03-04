
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {

	static int N;

	static String[] arr;

	static int normalResult = 0;
	static int abnormalResult = 0;

	static Queue<point> queue = new LinkedList<>();

	static int[][] visited;

	static int[] mx = {0, 0, 1, -1};
	static int[] my = {1, -1, 0, 0};

	static class point {
		int x, y;

		point(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		N = Integer.parseInt(br.readLine());
		arr = new String[N];
		visited = new int[N][N];

		for (int i = 0; i < N; i++) {
			arr[i] = br.readLine();
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				char tmp = arr[i].charAt(j);
				if (visited[i][j] == 0) {
					if ('R' == tmp) {
						bfs('R', i, j);
						normalResult++;
					} else if ('G' == tmp) {
						bfs('G', i, j);
						normalResult++;
					} else {
						bfs('B', i, j);
						normalResult++;
					}
				}
			}
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				String tmp = String.valueOf(arr[i].charAt(j));
				if ("G".equals(tmp)) {
					char[] chars = arr[i].toCharArray();
					chars[j] = 'R';
					arr[i] = new String(chars);
				}
			}
		}

		visited = new int[N][N];

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				char tmp = arr[i].charAt(j);
				if (visited[i][j] == 0) {
					if ('R' == tmp) {
						bfs('R', i, j);
						abnormalResult++;
					} else {
						bfs('B', i, j);
						abnormalResult++;
					}
				}
			}
		}

		System.out.print(normalResult + " " + abnormalResult);
	}

	private static void bfs(char typ, int x, int y) {
		queue.add(new point(x, y));
		visited[x][y] = 1;

		while (!queue.isEmpty()) {
			point p = queue.poll();
			int tmpX = p.x;
			int tmpY = p.y;

			for (int i = 0; i < 4; i++) {
				int dx = tmpX + mx[i];
				int dy = tmpY + my[i];

				if (0 <= dx && dx < N && 0 <= dy && dy < N) {
					if (visited[dx][dy] == 0 && typ == arr[dx].charAt(dy)) {
						queue.add(new point(dx, dy));
						visited[dx][dy] = 1;
					}
				}
			}
		}
	}

}