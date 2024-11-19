import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter br = new BufferedWriter(new OutputStreamWriter(System.out));
		int t = Integer.parseInt(sc.readLine());
		StringTokenizer st;
		for (int i = 0; i < t; i++) {
			st = new StringTokenizer(sc.readLine(), " ");
			br.write((Integer.parseInt(st.nextToken()) + Integer.parseInt(st.nextToken())) + "\n");
		}
		sc.close();
		br.flush();
		br.close();
	}
}