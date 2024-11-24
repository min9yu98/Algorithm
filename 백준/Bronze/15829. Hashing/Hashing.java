import java.io.*;
import java.util.Map;
import java.util.HashMap;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int n = Integer.parseInt(br.readLine());
		String words = br.readLine();

		Map<Character, Integer> map = new HashMap<>();
		for (int i = 97; i <= 122; i++) {
			map.put((char) i, i - 96);
		}

		long ans = 0L, tmp;
		for (int i = 0; i < n; i++) {
			tmp = map.get(words.charAt(i));
			for (int j = 0; j < i; j++) {
				tmp *= 31;
				tmp %= 1234567891;
			}
			ans += tmp % 1234567891;
		}

		bw.write(ans + "\n");

		br.close();
		bw.flush();
		bw.close();
	}
}