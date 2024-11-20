import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] arr = new int[9];
		int ans = -1;
		int idx = -1;
		for (int i = 0; i < 9; i++) {
			arr[i] = sc.nextInt();
			if (ans < arr[i]) {
				ans = arr[i];
				idx = i;
			}
		}
		System.out.println(ans);
		System.out.println(idx + 1);
	}
}