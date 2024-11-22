import java.io.*;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int n = Integer.parseInt(br.readLine());
		int[] arr = new int[6];

		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < 6; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		st = new StringTokenizer(br.readLine());
		int t = Integer.parseInt(st.nextToken()), p = Integer.parseInt(st.nextToken());

		int ans = 0;
		for (int i = 0; i < 6; i++) {
			ans += arr[i] / t;
			ans += arr[i] % t > 0 ? 1 : 0;
		}

		bw.write(ans + "\n");
		bw.write(n / p + " " + n % p);

		br.close();
		bw.flush();
		bw.close();
	}
}