
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		String s = br.readLine();
		StringBuilder check = new StringBuilder("I");
		for (int i = 0; i < N; i++) {
			check.append("OI");
		}

		int result = 0;
		int idx = 0;
		while ((idx = s.indexOf(String.valueOf(check), idx)) != -1) {
			result++;
			idx++;
		}

		System.out.println(result);
	}
}