import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] arr = new int[n];
		for (int i = 0; i < n; i++){
			arr[i] = sc.nextInt();
		}
		int v = sc.nextInt();
		int ans = 0;
		for (int k: arr) {
			if (v == k) {
				ans += 1;
			}
		}
		System.out.println(ans);
	}
}