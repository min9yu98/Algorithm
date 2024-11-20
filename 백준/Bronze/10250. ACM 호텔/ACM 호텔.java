import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for (int i = 0; i < t; i++) {
			int h = sc.nextInt(), w = sc.nextInt(), n = sc.nextInt();
			for (int j = 0; j < w; j++) {
				boolean flag = false;
				for (int k = 0; k < h; k++) {
					n--;
					if (n == 0) {
						System.out.println((k + 1) * 100 + j + 1);
						flag = true;
						break;
					}
				}
				if (flag) {
					break;
				}
			}
		}
	}
}