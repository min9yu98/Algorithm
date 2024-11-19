import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.next();
		for (int i = 0; i < s.length(); i++) {
			if ((int) s.charAt(i) >= 65 && (int) s.charAt(i) <= 90) {
				System.out.print((char) ((int) s.charAt(i) + 32));
			} else {
				System.out.print((char) ((int) s.charAt(i) - 32));
			}
		}
	}
}