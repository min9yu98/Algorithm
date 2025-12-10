
import java.io.*;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[20000001];
		StringTokenizer st = new StringTokenizer(br.readLine());;
		for (int i = 0; i < N; i++) {
			int x = Integer.parseInt(st.nextToken());
			arr[x + 10000000]++;
		}
		int M = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < M; i++) {
			int x = Integer.parseInt(st.nextToken());
			sb.append(arr[x + 10000000]).append(' ');
		}
		System.out.println(sb);
	}
}