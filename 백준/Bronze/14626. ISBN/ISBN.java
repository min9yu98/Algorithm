
import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());
		String isbn = st.nextToken();

		int result = 0;
		int tmp = 0;
		for (int i = 0; i < 13; i++) {
			if ("*".equals(String.valueOf(isbn.charAt(i)))) {
				continue;
			}
			if (i % 2 == 0) tmp += Character.getNumericValue(isbn.charAt(i));
			else tmp += (Character.getNumericValue(isbn.charAt(i)) * 3);
		}

		boolean isOdd = isbn.indexOf("*") % 2 == 0;

		while (true) {
			if (isbn.indexOf("*") % 2 == 0) {
				if ((tmp + result) % 10 == 0) {
					break;
				}
			} else {
				if ((tmp + result * 3) % 10 == 0) {
					break;
				}
			}
			result++;
		}

		sb.append(result);
		System.out.println(sb);
	}
}
