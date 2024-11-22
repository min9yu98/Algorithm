import java.io.*;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int n = Integer.parseInt(br.readLine());

		StringTokenizer st = new StringTokenizer(br.readLine());
		int[] arr = new int[n];
		int ans = 0;
		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
			if (sosu(arr[i])) {
				ans++;
			}
		}
		bw.write(ans + "\n");

		br.close();
		bw.flush();
		bw.close();
	}

	public static boolean sosu(int k) {
		boolean flag = true;
		if (k <= 1) {
			return false;
		}
		for (int i = 2; i <= Math.sqrt(k); i++) {
			if (k % i == 0) {
				flag = false;
				break;
			}
		}
		return flag;
	}
}