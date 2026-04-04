
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		long M = Long.parseLong(st.nextToken());
		long[] arr = new long[N];

		long std = 0;
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			arr[i] = Long.parseLong(st.nextToken());
			if (std < arr[i]) {
				std = arr[i];
			}
		}

		long start = 0;
		long end = std;
		long result = 0;
		while (start <= end) {
			long mid = (start + end) / 2;

			long tmp = 0;
			for (int i = 0; i < N; i++) {
				if (arr[i] - mid > 0) tmp += arr[i] - mid;
			}

			if (tmp >= M) {
				start = mid + 1;
				result = mid;
			} else {
				end = mid - 1;
			}
		}

		System.out.println(result);
	}

}