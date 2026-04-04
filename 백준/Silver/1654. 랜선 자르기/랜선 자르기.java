
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int K = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());

		long t = 0;
		long[] arr = new long[K];
		for (int i = 0; i < K; i++) {
			arr[i] = Long.parseLong(br.readLine());
			if (t < arr[i]) t = arr[i];
		}

		long result = 0;
		long start = 1;
		long end = t;
		while (start <= end) {
			long mid = (start + end) / 2;

			long tmp = 0;
			for (int i = 0; i < K; i++) {
				tmp += (int)(arr[i] / mid);
			}

			if (N > tmp) {
				end = mid  - 1;
			} else {
				result = Math.max(mid, result);
				start = mid + 1;
			}
		}

		System.out.println(result);
	}

}