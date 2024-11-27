import java.io.*;

public class Main {

	static int[] arr = new int[301];
	static int[] dp = new int[301];

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}

		dp[0] = arr[0];
		dp[1] = Math.max(arr[0] + arr[1], arr[1]);
		dp[2] = Math.max(arr[0] + arr[2], arr[1] + arr[2]);

		for (int i = 3; i < n; i++) {
			dp[i] = Math.max(arr[i] + dp[i - 2], arr[i] + arr[i - 1] + dp[i - 3]);
		}

		System.out.println(dp[n - 1]);

	}

}
