import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] arr = new int[8];
		for (int i = 0; i < 8; i++) {
			arr[i] = sc.nextInt();
		}
		boolean asc = false, desc = false;
		for (int i = 0; i < 7; i++) {
			if (arr[i] < arr[i + 1]) {
				asc = true;
			} else if (arr[i] > arr[i + 1]) {
				desc = true;
			}
		}
		if (asc && !desc) {
			System.out.println("ascending");
		} else if (!asc && desc) {
			System.out.println("descending");
		} else {
			System.out.println("mixed");
		}
	}
}