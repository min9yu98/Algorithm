
import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());

		int count = 1;
		int devil = 666;
		while (count != n) {
			devil++;

			if (String.valueOf(devil).contains("666")) {
				count++;
			}
		}
		System.out.println(devil);
	}
}