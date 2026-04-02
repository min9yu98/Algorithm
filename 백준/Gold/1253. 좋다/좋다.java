
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int cnt = 0;
		int N = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());

		int[] arr = new int[N];
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}

		Arrays.sort(arr);

		for (int i = 0; i < N; i++) {
			int start = 0;
			int end = N - 1;

			while (start < end) {
				if (start == i || end == i) {
					if (start == i) start++;
					else end--;
				} else {
					int sum = arr[start] + arr[end];

					if (sum > arr[i]) end--;
					else if (sum == arr[i]) {
						cnt++;
						break;
					}
					else start++;
				}
			}
		}

		System.out.println(cnt);

	}


}



