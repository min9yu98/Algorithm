
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
		char s[] = br.readLine().toCharArray();

		int result = 0;
		int cnt = 0;
		for (int i = 1; i < M - 1; i++) {
			if (s[i - 1] == 'I' && s[i] == 'O' && s[i + 1] == 'I') {
				cnt++;
				if (cnt == N) {
					cnt--;
					result++;
				}
				i++;
			} else {
				cnt = 0;
			}
		}

		System.out.println(result);
	}
}