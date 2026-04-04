
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int stick = 64;

		int result = 0;
		for (int i = 0; i < 7; i++) {
			if ((N & 1 << i) > 0) result++;
		}
		System.out.println(result);
	}

}