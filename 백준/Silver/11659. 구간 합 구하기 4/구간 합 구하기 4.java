import java.io.*;
import java.util.StringTokenizer;

public class Main {

	static int[] arr;
	static int[] cul;

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
		arr = new int[n + 1];
		cul = new int[n + 1];
		st = new StringTokenizer(br.readLine());
		arr[0] = 0;
		for (int i = 1; i <= n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		cul[0] = 0;
		cul[1] = arr[1];
		for (int i = 1; i <= n; i++) {
			cul[i] = arr[i] + cul[i - 1];
		}

		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken()), b = Integer.parseInt(st.nextToken());
			System.out.println(cul[b] - cul[a - 1]);
		}
	}

}
