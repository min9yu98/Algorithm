
import java.io.*;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(br.readLine());
		boolean[] disappear = new boolean[n + 1];
		Stack<Integer> stack = new Stack<>();
		int tmp = 0;
		for (int ord = 0; ord < n; ord++) {
			int k = Integer.parseInt(br.readLine());
			if (ord == 0) {
				for (int i = 1; i <= k; i++) {
					stack.push(i);
					sb.append("+\n");
				}
				tmp = k;
			}

			if (tmp >= k) {
				if (disappear[k]) {
					System.out.println("NO");
					return;
				}
				while (!stack.isEmpty()) {
					int top = stack.pop();
					disappear[top] = true;
					sb.append("-\n");
					if (top == k) {
						break;
					}
				}
			} else {
				for (int i = tmp + 1; i <= k; i++) {
					stack.push(i);
					sb.append("+\n");
				}
				tmp = k;
				int top = stack.pop();
				disappear[top] = true;
				sb.append("-\n");
			}

		}
		System.out.println(sb);
	}

}