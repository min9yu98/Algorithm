
import java.io.*;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for (int i = 0; i < T; i++) {
			String input = br.readLine();
			sb.append(solve(input)).append('\n');
		}
		System.out.println(sb);
	}

	public static String solve(String input) {
		Stack<Character> stack = new Stack<>();

		for (int i = 0; i < input.length(); i++) {
			char ch = input.charAt(i);
			if (ch == '(') {
				stack.push(ch);
			} else {
				if (stack.isEmpty() || stack.peek() != '(') {
					return "NO";
				} else {
					stack.pop();
				}
			}
		}

		if (stack.isEmpty()) return "YES";
		else return "NO";
	}
}