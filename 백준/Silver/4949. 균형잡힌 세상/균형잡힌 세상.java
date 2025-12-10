
import java.io.*;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		String input;
		while (true) {
			input = br.readLine();

			if (input.equals(".")) break;
			sb.append(solve(input)).append('\n');
		}
		System.out.println(sb);
	}

	public static String solve(String input) {
		Stack<Character> stack = new Stack<>();

		for (int i = 0; i < input.length(); i++) {
			char ch = input.charAt(i);
			if (ch == '(' || ch == '[') {
				stack.push(ch);
			} else if (ch == ')') {
				if (stack.isEmpty() || stack.peek() != '(') {
					return "no";
				} else {
					stack.pop();
				}
			} else if (ch == ']') {
				if (stack.isEmpty() || stack.peek() != '[') {
					return "no";
				} else {
					stack.pop();
				}
			}
		}

		if (stack.isEmpty()) return "yes";
		else return "no";
	}
}