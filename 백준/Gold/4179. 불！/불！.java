import java.io.*;
import java.util.*;

public class Main {

	static int[][] miro;
	static int[][] fire;
	static int[][] person;
	static boolean[][] visited;
	static boolean[][] fireVisited;
	static int[] dx = {0, 0, -1, 1};
	static int[] dy = {1, -1, 0, 0};

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int r = Integer.parseInt(st.nextToken()), c = Integer.parseInt(st.nextToken());
		miro = new int[r][c];
		fire = new int[r][c];
		int f_x = 0, f_y = 0;
		person = new int[r][c];
		int p_x = 0, p_y = 0;
		visited = new boolean[r][c];
		fireVisited = new boolean[r][c];

		Queue<int[]> fireQ = new LinkedList<>();
		Queue<int[]> q = new LinkedList<>();
		for (int i = 0; i < r; i++) {
			String s = br.readLine();
			for (int j = 0; j < c; j++) {
				miro[i][j] = s.charAt(j);
				person[i][j] = 0;
				fire[i][j] = 0;
				visited[i][j] = false;
				fireVisited[i][j] = false;
				if (miro[i][j] == 'F') {
					fire[i][j] = 1;
					fireVisited[i][j] = true;
					fireQ.offer(new int[] {i, j});
				}
				if (miro[i][j] == 'J') {
					person[i][j] = 1;
					visited[i][j] = true;
					q.offer(new int[] {i, j});
				}
			}
		}

		while (!fireQ.isEmpty()) {
			int[] cur = fireQ.poll();
			int x = cur[0];
			int y = cur[1];
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (0 <= nx && nx < r && 0 <= ny && ny < c) {
					if (miro[nx][ny] !='#' && !fireVisited[nx][ny]) {
						fire[nx][ny] = fire[x][y] + 1;
						fireVisited[nx][ny] = true;
						fireQ.offer(new int[] {nx, ny});
					}
				}
			}
		}

		// int min = Integer.MAX_VALUE;
		while (!q.isEmpty()) {
			int[] cur = q.poll();
			int x = cur[0];
			int y = cur[1];
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (0 <= nx && nx < r && 0 <= ny && ny < c) {
					if (miro[nx][ny] == '.' && !visited[nx][ny]) {
						person[nx][ny] = person[x][y] + 1;
						visited[nx][ny] = true;
						q.offer(new int[] {nx, ny});
					}
				}
			}
		}

		int min = Integer.MAX_VALUE;
		for (int i = 0; i < c; i++) {
			if ((fire[0][i] == 0 && person[0][i] != 0) || (fire[0][i] > person[0][i] && person[0][i] != 0)) {
				min = Math.min(min, person[0][i]);
			}
			if ((fire[r - 1][i] == 0 && person[r - 1][i] != 0) || (fire[r - 1][i] > person[r - 1][i] && person[r - 1][i] != 0)) {
				min = Math.min(min, person[r - 1][i]);
			}
		}

		for (int i = 0; i < r; i++) {
			if ((fire[i][0] == 0 && person[i][0] != 0) || (fire[i][0] > person[i][0] && person[i][0] != 0)) {
				min = Math.min(min, person[i][0]);
			}
			if ((fire[i][c - 1] == 0 && person[i][c - 1] != 0) || (fire[i][c - 1] > person[i][c - 1] && person[i][c - 1] != 0)) {
				min = Math.min(min, person[i][c - 1]);
			}
		}

		System.out.println(min == Integer.MAX_VALUE ? "IMPOSSIBLE" : min);

	}
}
