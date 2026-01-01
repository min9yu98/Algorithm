
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

	static int black = 0;
	static int white = 0;
	static int[][] board;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st;
		board = new int[N][N];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		partition(0, 0, N);

		System.out.println(white);
		System.out.println(black);
	}

	private static void partition(int row, int col, int size) {
		if (colorCheck(row, col, size)) {
			if (board[row][col] == 0) {
				white++;
			} else {
				black++;
			}
			return;
		}

		int newSize = size / 2;

		partition(row, col, newSize);
		partition(row, col + newSize, newSize);
		partition(row + newSize, col, newSize);
		partition(row + newSize, col + newSize, newSize);
	}

	private static boolean colorCheck(int row, int col, int size) {
		int color = board[row][col];
		for (int i = row; i < row + size; i++) {
			for (int j = col; j < col + size; j++) {
				if (board[i][j] != color) {
					return false;
				}
			}
		}
		return true;
	}


}