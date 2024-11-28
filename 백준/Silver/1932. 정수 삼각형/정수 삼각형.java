import java.io.*;
import java.util.*;

public class Main {

	static int[][] dp;
	static int[][] arr;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		arr = new int[n][n];
		dp = new int[n][n];
		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j <= i; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		dp[0][0] = arr[0][0];
		for (int i = 0; i < n - 1; i++) {
			for (int j = 0; j <= i; j++) {
				dp[i + 1][j] = Math.max(dp[i + 1][j], dp[i][j] + arr[i + 1][j]);
				dp[i + 1][j + 1] = Math.max(dp[i + 1][j + 1], dp[i][j] + arr[i + 1][j + 1]);
			}
		}
		int[] result = dp[n - 1];
		System.out.println(Arrays.stream(result).max().getAsInt());
	}

}
