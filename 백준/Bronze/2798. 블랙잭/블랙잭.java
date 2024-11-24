import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
		int[] cards = new int[n];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			cards[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(cards);
		int ans = 0, score;
		for (int i = n - 1; i > -1; i--) {
			for (int j = i - 1; j > -1; j--) {
				for (int k = j - 1; k > -1; k--) {
					score = cards[i] + cards[j] + cards[k];
					if (score <= m) {
						ans = Math.max(ans, score);
					}
				}
			}
		}
		bw.write(ans + "\n");

		br.close();
		bw.flush();
		bw.close();
	}
}