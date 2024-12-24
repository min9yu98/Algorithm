import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st;
		Set<Integer> map = new HashSet<>();
		int bit = 0;
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			String input = st.nextToken();
			if (input.equals("all")) {
				bit = (1 << 21) - 1;
				continue;
			} else if (input.equals("empty")) {
				bit = 0;
				continue;
			}
			int num = Integer.parseInt(st.nextToken());
			switch (input) {
				case "add":
					bit |= (1 << num);
					break;
				case "remove":
					bit &= ~(1 << num);
					break;
				case "check":
					sb.append((bit & (1 << num)) != 0 ? 1 : 0).append("\n");
					break;
				case "toggle":
					bit ^= (1 << num);
					break;
				default:
					break;
			}
		}
		System.out.println(sb);
	}
}
