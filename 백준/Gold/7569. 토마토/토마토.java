
import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int m, n, h;
	static int[][][] arr;
	static int[] nx = {0, 0, 1, -1, 0, 0};
	static int[] ny = {1, -1, 0, 0, 0, 0};
	static int[] nz = {0, 0, 0, 0, 1, -1};
	static Queue<point> q = new LinkedList<>();

	static class point {
		int x, y, z; // n, m, h

		point(int x, int y, int z) {
			this.x = x;
			this.y = y;
			this.z = z;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		m = Integer.parseInt(st.nextToken()); // 가로
		n = Integer.parseInt(st.nextToken()); // 세로
		h = Integer.parseInt(st.nextToken()); // 높이

		arr = new int[h][n][m];
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < n; j++) {
				st = new StringTokenizer(br.readLine());
				for (int k = 0; k < m; k++) {
					arr[i][j][k] = Integer.parseInt(st.nextToken());
					if (arr[i][j][k] == 1) {
						q.add(new point(j, k, i));
					}
				}
			}
		}

		bfs();
		checkArr();
	}

	private static void bfs() {
		while (!q.isEmpty()) {
			point p = q.poll();
			int x = p.x;
			int y = p.y;
			int z = p.z;

			for (int i = 0; i < 6; i++) {
				int mx = x + nx[i];
				int my = y + ny[i];
				int mz = z + nz[i];

				if (0 <= mx && mx < n && 0 <= my && my < m && 0 <= mz && mz < h) {
					if (arr[mz][mx][my] == 0) {
						arr[mz][mx][my] = arr[z][x][y] + 1;
						q.add(new point(mx, my, mz));
					}
				}
			}
		}
	}

	private static void checkArr() {
		int max = 0;

		for (int i = 0; i < h; i++) {
			for (int j = 0; j < n; j++) {
				for (int k = 0; k < m; k++) {
					if (arr[i][j][k] == 0) {
						System.out.println(-1);
						return;
					}
					max = Math.max(arr[i][j][k], max);
				}
			}
		}
		System.out.println(max - 1);
	}

}