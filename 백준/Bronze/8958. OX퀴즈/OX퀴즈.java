import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for (int i = 0; i < t; i++) {
			String s = sc.next();
			int score = 0;
			int tmp = 1;
			for (int j = 0; j < s.length(); j++) {
				if (s.charAt(j) == 'O') {
					score += tmp;
					tmp ++;
				} else {
					tmp = 1;
				}
			}
			System.out.println(score);
		}
	}
}