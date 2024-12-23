import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		while (true) {
			st = new StringTokenizer(br.readLine());
			int[] lst = new int[3];
			for (int i = 0; i < 3; i++) {
				lst[i] = Integer.parseInt(st.nextToken());
			}
			Arrays.sort(lst);
			if (lst[0] == lst[2] && lst[2] == 0) {
				break;
			}
			if (lst[2] >= lst[0] + lst[1]) {
				System.out.println("Invalid");
				continue;
			}
			if (lst[0] == lst[2]) {
				System.out.println("Equilateral");
			} else if ((lst[0] == lst[1] && lst[1] != lst[2]) || (lst[0] != lst[1] && lst[1] == lst[2])) {
				System.out.println("Isosceles");
			} else if (lst[0] != lst[1] && lst[1] != lst[2]) {
				System.out.println("Scalene");
			}
		}
	}
}