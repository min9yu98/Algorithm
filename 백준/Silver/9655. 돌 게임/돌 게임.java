import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int tmp = n / 3 + n % 3;
		if (tmp % 2 == 0) {
			System.out.println("CY");
		} else {
			System.out.println("SK");
		}
	}
}