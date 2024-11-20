import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long n = sc.nextLong();
		long mini = 1000000001;
		long maxi = -1000000001;
		for (int i = 0; i < n; i++) {
			long tmp = sc.nextLong();
			mini = Math.min(tmp, mini);
			maxi = Math.max(tmp, maxi);
		}
		System.out.println(mini + " " + maxi);
	}
}