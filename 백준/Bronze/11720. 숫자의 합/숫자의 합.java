import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		String num = sc.next();
		int total = 0;
		for (int i = 0; i < n; i++) {
			total += num.charAt(i) - '0';
		}
		System.out.println(total);
	}
}