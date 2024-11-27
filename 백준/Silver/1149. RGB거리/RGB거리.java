import java.io.*;

public class Main {

	static int[][] arr;
	static int[][] dp;

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());
		arr = new int[n][3];
		dp = new int[n][3];
		for (int i = 0; i < n; i++) {
			String[] s = br.readLine().split(" ");
			arr[i][0] = Integer.parseInt(s[0]);
			arr[i][1] = Integer.parseInt(s[1]);
			arr[i][2] = Integer.parseInt(s[2]);
			dp[i][0] = Integer.MAX_VALUE;
			dp[i][1] = Integer.MAX_VALUE;
			dp[i][2] = Integer.MAX_VALUE;
		}
		dp[0][0] = arr[0][0];
		dp[0][1] = arr[0][1];
		dp[0][2] = arr[0][2];
		for (int i = 1; i < n; i++) {
			dp[i][0] = Math.min(dp[i - 1][1] + arr[i][0], dp[i - 1][2] + arr[i][0]);
			dp[i][1] = Math.min(dp[i - 1][0] + arr[i][1], dp[i - 1][2] + arr[i][1]);
			dp[i][2] = Math.min(dp[i - 1][0] + arr[i][2], dp[i - 1][1] + arr[i][2]);
		}
		System.out.println(Math.min(dp[n - 1][0], Math.min(dp[n - 1][1], dp[n - 1][2])));
	}

}
