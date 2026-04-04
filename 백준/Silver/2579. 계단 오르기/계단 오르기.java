
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.io.IOException;

public class Main {

	static int N;
	static Integer[] dp;
	static int[] arr;


	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		arr = new int[N + 1];
		dp = new Integer[N + 1];

		for (int i = 1; i < N + 1; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}

		dp[0] = arr[0];
		dp[1] = arr[1];

		if (N >= 2) {
			dp[2] = arr[1] + arr[2];
		}

		System.out.println(find(N));
	}

	private static int find(int n) {
		if (dp[n] == null) {
			dp[n] = Math.max(find(n - 2), find(n - 3) + arr[n - 1]) + arr[n];
		}

		return dp[n];
	}
}

