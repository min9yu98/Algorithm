import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());

		int T = Integer.parseInt(st.nextToken());
		for (int i = 0; i < T; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());

			int tmp = 1;
			for (int j = 0; j < b; j++) {
				tmp *= a;
				tmp %= 10;
			}
			if (tmp % 10 == 0) {
				sb.append(10).append('\n');
				continue;
			}
			sb.append(tmp % 10).append('\n');
		}
		System.out.println(sb);
	}
}
