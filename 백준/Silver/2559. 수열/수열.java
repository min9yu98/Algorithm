
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		int[] arr = new int[N + 1];
		int[] hap = new int[N + 1];

		st = new StringTokenizer(br.readLine());
		for (int i = 1; i < N + 1; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
			hap[i] = hap[i - 1] + arr[i];
		}

		int max = Integer.MIN_VALUE;
		for (int i = K; i < N + 1; i++) {
			int t = hap[i] - hap[i - K];
			if (max < t) {
				max = t;
			}
		}

		System.out.println(max);
	}

}