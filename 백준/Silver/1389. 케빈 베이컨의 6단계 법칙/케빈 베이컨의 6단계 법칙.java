
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static final int INF = 987654321;

	static int N;
	static int M;
	static int[][] rel;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		rel = new int[N + 1][N + 1];
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if (i == j) {
					rel[i][j] = 0;
				} else {
					rel[i][j] = INF;
				}
			}
		}
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			rel[x][y] = 1;
			rel[y][x] = 1;
		}

		for (int k = 1; k <= N; k++) {
			for (int i = 1; i <= N; i++) {
				for (int j = 1; j <= N; j++) {
					if (rel[i][j] > rel[i][k] + rel[k][j]) {
						rel[i][j] = rel[i][k] + rel[k][j];
					}
				}
			}
		}

		int result = INF;
		int idx = -1;

		for (int i = 1; i <= N; i++) {
			int total = 0;
			for (int j = 1; j <= N; j++) {
				total += rel[i][j];
			}

			if (result > total) {
				result = total;
				idx = i;
			}
		}

		System.out.println(idx);
	}
}