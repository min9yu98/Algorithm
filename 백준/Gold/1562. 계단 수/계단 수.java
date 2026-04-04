
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int MOD = 1000000000;
		long[][][] dp = new long[N + 1][10][1 << 10];

		for (int i = 1; i <= 9; i++) {
			dp[1][i][1 << i] = 1;
		}

		for (int len = 1; len < N; len++) {
			for (int digit = 0; digit <= 9; digit++) {
				for (int mask = 0; mask < (1 << 10); mask++) {
					long cur = dp[len][digit][mask];

					if (cur == 0) continue;

					if (digit > 0) {
						int next = digit - 1;
						int newMask = mask | (1 << next);
						dp[len + 1][next][newMask] = (dp[len + 1][next][newMask] + cur) % MOD;
					}

					if (digit < 9) {
						int next = digit + 1;
						int newMask = mask | (1 << next);
						dp[len + 1][next][newMask] = (dp[len + 1][next][newMask] + cur) % MOD;
					}
				}
			}
		}

		int fullMask = (1 << 10) - 1;
		long answer = 0;

		for (int digit = 0; digit <= 9; digit++) {
			answer = (answer + dp[N][digit][fullMask]) % MOD;
		}

		System.out.println(answer);
	}

}