
import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(br.readLine());
		int result = 0;
		int[] arr = new int[6000];
		Arrays.fill(arr, -1);
		arr[3] = 1;
		arr[5] = 1;
		arr[6] = 2;
		arr[8] = 2;
		arr[9] = 3;
		arr[10] = 2;
		arr[11] = 3;
		arr[12] = 4;
		if (N < 13) {
			System.out.println(arr[N]);
			return;
		}
		for (int i = 13; i <= N; i++) {
			arr[i] = arr[i - 5] + 1;
		}
		System.out.println(arr[N]);
	}
}