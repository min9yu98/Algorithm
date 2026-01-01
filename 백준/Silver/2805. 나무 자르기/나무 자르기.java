
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {


	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int[] arr = new int[N];
		st = new StringTokenizer(br.readLine());
		int maxi = 0;
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
			if (maxi < arr[i]) maxi = arr[i];
		}

		maxi++;
		int mini = 0;
		while (mini <= maxi) {
			int mid = (maxi + mini) / 2;

			long tmp = 0;
			for (int i = 0; i < N; i++) {
				if (mid < arr[i]) {
					tmp += arr[i] - mid;
				}
			}

			if (tmp < M) {
				maxi = mid - 1;
			} else {
				mini = mid + 1;
			}
		}
		System.out.println(mini - 1);
	}
}