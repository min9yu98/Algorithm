
import java.io.*;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	private static boolean[][] arr;
	private static int min = Integer.MAX_VALUE;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		arr = new boolean[N][M];
		for (int i = 0; i < N; i++) {
			String str = br.readLine();
			for (int j = 0; j < M; j++) {
				arr[i][j] = str.charAt(j) == 'B';
			}
		}

		int w = N - 7;
		int h = M - 7;

		for (int i = 0; i < w; i++) {
			for (int j = 0; j < h; j++) {
				findMin(i, j);
			}
		}

		System.out.println(min);
	}

	public static void findMin(int x, int y) {
		int endX = x + 8;
		int endY = y + 8;
		int cnt = 0;

		boolean stand = arr[x][y];

		for (int i = x; i < endX; i++) {
			for (int j = y; j < endY; j++) {
				if (arr[i][j] != stand) {
					cnt++;
				}
				stand = !stand;
			}
			stand = !stand;
		}

		cnt = Math.min(cnt, 64 - cnt);
		min = Math.min(min, cnt);
	}
}