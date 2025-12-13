
import java.io.*;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[N];
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		Arrays.sort(arr);

		int mod = arr[0];
		boolean check = false;
		int cnt = 0;
		int max = -1;
		for (int i = 0; i < N - 1; i++) {
			if (arr[i] == arr[i + 1]) {
				cnt++;
			} else {
				cnt = 0;
			}

			if (max < cnt) {
				max = cnt;
				mod = arr[i];
				check = true;
			} else if (max == cnt && check) {
				mod = arr[i];
				check = false;
			}
		}


		double avg = Arrays.stream(arr).average().orElse(0.0);
		System.out.println((int) Math.round(avg));
		System.out.println(arr[(N - 1) / 2]);
		System.out.println(mod);
		System.out.println(arr[N - 1] - arr[0]);
	}

}