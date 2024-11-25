import java.io.*;
import java.util.*;

public class Main {


	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st;
		Queue<Integer> q = new LinkedList<>();
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			String command = st.nextToken();
			if (command.equals("push")) {
				int num = Integer.parseInt(st.nextToken());
				q.offer(num);
			} else if (command.equals("front")) {
				if (q.isEmpty()) {
					System.out.println(-1);
				} else {
					System.out.println(q.peek());
				}
			} else if (command.equals("back")) {
				if (q.isEmpty()) {
					System.out.println(-1);
				} else {
					int size = q.size();
					int back = 0;
					for (int j = 0; j < size; j++) {
						back = q.poll();
						q.offer(back);
					}
					System.out.println(back);
				}
			} else if (command.equals("size")) {
				System.out.println(q.size());
			} else if (command.equals("empty")) {
				if (q.isEmpty()) {
					System.out.println(1);
				} else {
					System.out.println(0);
				}
			} else if (command.equals("pop")) {
				if (q.isEmpty()) {
					System.out.println(-1);
				} else {
					System.out.println(q.poll());
				}
			}
		}
	}
}
