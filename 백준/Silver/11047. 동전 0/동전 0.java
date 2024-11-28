import java.io.*;
import java.util.*;

public class Main {

	static int[] coins;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken()), k = Integer.parseInt(st.nextToken());
		coins = new int[n];
		for (int i = 0; i < n; i++) {
			coins[i] = Integer.parseInt(br.readLine());
		}
		int ans = 0;
		for (int i = n - 1; i >= 0; i--) {
			if (k < coins[i]) {
				continue;
			}
			ans += k / coins[i];
			k %= coins[i];
		}
		System.out.println(ans);

	}
}
