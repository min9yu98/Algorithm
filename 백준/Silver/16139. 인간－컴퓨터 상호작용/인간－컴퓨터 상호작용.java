
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		String S = br.readLine();
		int q = Integer.parseInt(br.readLine());
		int[][] prefix = new int[26][S.length() + 1];

		for (int i = 1; i < S.length() + 1; i++) {
			char c = S.charAt(i - 1);
			for (int j = 0; j < 26; j++) {
				prefix[j][i] = prefix[j][i - 1];
			}
			prefix[c - 'a'][i]++;
		}

		for (int x = 0; x < q; x++) {
			st = new StringTokenizer(br.readLine());
			char a = st.nextToken().charAt(0);
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());

			System.out.println(prefix[a - 'a'][end + 1] - prefix[a - 'a'][start]);
		}
	}

}