
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	public static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());

		ArrayDeque<Integer> deque;
		StringTokenizer st;
		for (int ord = 0; ord < T; ord++) {
			String com = br.readLine();
			int n = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine(), "[],");
			deque = new ArrayDeque<>();

			for (int i = 0; i < n; i++) {
				deque.add(Integer.parseInt(st.nextToken()));
			}

			ac(com, deque);
		}
		System.out.println(sb);
	}

	private static void ac(String com, ArrayDeque<Integer> deque) {
		boolean isRight = true;
		for (char c : com.toCharArray()) {
			if (c == 'R') {
				isRight = !isRight;
				continue;
			}

			if (isRight) {
				if (deque.pollFirst() == null) {
					sb.append("error\n");
					return;
				}
			} else {
				if (deque.pollLast() == null) {
					sb.append("error\n");
					return;
				}
			}
		}

		makePrint(deque, isRight);
	}

	private static void makePrint(ArrayDeque<Integer> deque, boolean isRight) {
		sb.append('[');
		if (!deque.isEmpty()) {
			if (isRight) {
				sb.append(deque.pollFirst());
				while (!deque.isEmpty()) {
					sb.append(',').append(deque.pollFirst());
				}
			} else {
				sb.append(deque.pollLast());
				while (!deque.isEmpty()) {
					sb.append(',').append(deque.pollLast());
				}
			}
		}
		sb.append(']').append('\n');
	}
}