import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Map<Integer, Integer> homework = new HashMap<>();
		for (int i = 1; i <= 30; i++){
			homework.put(i, 1);
		}
		for (int i = 0; i < 28; i++) {
			int p = sc.nextInt();
			homework.put(p, homework.get(p) - 1);
		}
		for (int i = 1; i <= 30; i++) {
			if (homework.get(i) == 1) {
				System.out.println(i);
			}
		}
	}
}