
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int[] arr;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		arr = new int[N];

		int result = 0;
		int left = 0;
		int right = 0;
		for (int i = 0; i < N; i++) {
			int k = Integer.parseInt(br.readLine());
			arr[i] = k;
			left = Math.max(left, k);
			right += k;
		}

		while (left <= right) {
			int mid = (left + right) / 2;
			if (M >= getMid(mid)) {
				result = mid;
				right = mid - 1;
			} else {
				left = mid + 1;
			}
		}

		System.out.println(result);
	}

	private static int getMid(int tmp) {
		int cnt = 1;
		int money = tmp;

		for (int num : arr) {
			money -= num;

			if (money < 0) {
				cnt++;
				money = tmp - num;
			}
		}
		
		return cnt;
	}
}