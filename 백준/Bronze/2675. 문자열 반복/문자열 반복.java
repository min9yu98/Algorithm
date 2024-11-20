import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for (int i = 0; i < t; i++) {
			int r = sc.nextInt();
			String s = sc.next();
			String ans = "";
			for (int j = 0; j < s.length(); j++) {
				for (int k = 0; k < r; k++) {
					ans += s.charAt(j);
				}
			}
			System.out.println(ans);
		}
	}
}