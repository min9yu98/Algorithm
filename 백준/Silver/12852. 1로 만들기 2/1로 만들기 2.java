import java.io.*;

public class Main {

	static int[] dp;
	static String[] dpString;

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		dp = new int[1000001];
		dpString = new String[1000001];
		dp[0] = 0;
		dp[1] = 0;
		dp[2] = 1;
		dp[3] = 1;
		dpString[0] = "0";
		dpString[1] = "1";
		dpString[2] = "1 2";
		dpString[3] = "1 3";
		for (int i = 4; i <= n; i++) {
			if (i % 2 == 0 && i % 3 == 0) {
				dp[i] = Math.min(dp[i / 2] + 1, dp[i / 3] + 1);
				if (dp[i / 2] < dp[i / 3]) {
					dpString[i] = dpString[i / 2] + " " + i;
				} else {
					dpString[i] = dpString[i / 3] + " " + i;
				}
			} else if (i % 3 == 0) {
				dp[i] = Math.min(dp[i / 3] + 1, dp[i - 1] + 1);
				if (dp[i / 3] < dp[i - 1]) {
					dpString[i] = dpString[i / 3] + " " + i;
				} else {
					dpString[i] = dpString[i - 1] + " " + i;
				}
			} else if (i % 2 == 0) {
				dp[i] = Math.min(dp[i / 2] + 1, dp[i - 1] + 1);
				if (dp[i / 2] < dp[i - 1]) {
					dpString[i] = dpString[i / 2] + " " + i;
				} else {
					dpString[i] = dpString[i - 1] + " " + i;
				}
			} else {
				dp[i] = dp[i - 1] + 1;
				dpString[i] = dpString[i - 1] + " " + i;
			}
		}
		System.out.println(dp[n]);
		String[] answer = dpString[n].split(" ");
		for (int i = answer.length - 1; i >= 0; i--) {
			System.out.print(answer[i] + " ");
		}
	}

}
