import java.io.*;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken()), k = Integer.parseInt(st.nextToken());
		int tmp = 1;
		for (int i = 1; i <= k; i++) {
			tmp *= (n - i + 1);
			tmp /= i;
		}
		bw.write(tmp + "\n");

		br.close();
		bw.flush();
		br.close();

	}
}
