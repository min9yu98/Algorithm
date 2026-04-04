
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		long result = 0;
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		long[] arr = new long[N + 1];
		long[] mod = new long[M];

		st = new StringTokenizer(br.readLine());
		for (int i = 1; i < N + 1; i++) {
			int input = Integer.parseInt(st.nextToken());
			arr[i] = (arr[i - 1] + input) % M;
			if (arr[i] % M == 0) {
				result++;
			}
			mod[(int) arr[i]]++;
		}

		for (int i = 0; i < M; i++) {
			if (mod[i] > 0) {
				result += ((mod[i] * (mod[i] - 1)) / 2);
			}
		}

		System.out.println(result);
	}

}