import java.io.*;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());

		int gcd = gcd(n, m);

		System.out.println(gcd);
		System.out.println((n * m) / gcd);
	}

	public static int gcd(int a, int b) {
		if (a % b == 0)
			return b;
		return gcd(b, a % b);
	}
}