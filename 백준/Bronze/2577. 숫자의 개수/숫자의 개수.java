import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt();
		String result = (a * b * c) + "";
		Map<Integer, Integer> map = new HashMap<>();
		for (int i = 0; i < 10; i++) {
			map.put(i, 0);
		}
		for (int i = 0; i < result.length(); i++) {
			int num = Integer.parseInt(result.charAt(i) + "");
			map.put(num, map.get(num) + 1);
		}
		for (int i = 0; i < 10; i++) {
			System.out.println(map.get(i));
		}
	}
}