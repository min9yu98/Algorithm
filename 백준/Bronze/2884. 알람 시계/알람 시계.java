import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int h = sc.nextInt(), m = sc.nextInt();
		int total = h * 60 + m;
		if (total < 45) {
			total += 24 * 60;
		}
		total -= 45;
		System.out.println(total / 60 + " " + total % 60);
	}
}