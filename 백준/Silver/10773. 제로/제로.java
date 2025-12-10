
import java.io.*;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int K = Integer.parseInt(br.readLine());
		Stack<Integer> stack = new Stack<>();

		for (int i = 0; i < K; i++) {
			int x = Integer.parseInt(br.readLine());
			if (x != 0) {
				stack.push(x);
			} else {
				if (!stack.isEmpty()) stack.pop();
			}
		}

		if (stack.isEmpty()) {
			System.out.println(0);
		} else {
			int sum = 0;
			for (int num : stack) {
				sum += num;
			}
			System.out.println(sum);
		}
	}
}