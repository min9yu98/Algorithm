
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int B = Integer.parseInt(st.nextToken());
		int[][] land = new int[N][M];
		int max = Integer.MIN_VALUE;
		int min = Integer.MAX_VALUE;
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				land[i][j] = Integer.parseInt(st.nextToken());
				if (max < land[i][j]) {
					max = land[i][j];
				}
				if (min > land[i][j]) {
					min = land[i][j];
				}
			}
		}

		int time = Integer.MAX_VALUE;
		int high = 0;

		for (int i = min; i <= max; i++) {
			int cnt = 0;
			int block = B;
			for (int x = 0; x < N; x++) {
				for (int y = 0; y < M; y++) {
					if (i < land[x][y]) {
						cnt += (land[x][y] - i) * 2;
						block += (land[x][y] - i);
					} else {
						cnt += (i - land[x][y]);
						block -= (i - land[x][y]);
					}
				}
			}
			if (block < 0) {
				break;
			}

			if (time >= cnt) {
				time = cnt;
				high = i;
			}
		}
		System.out.println(time + " " + high);
	}

}