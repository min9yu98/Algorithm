import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int n = Integer.parseInt(br.readLine());
		int[] scores = new int[n];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			scores[i] = Integer.parseInt(st.nextToken());
		}

		int m = Arrays.stream(scores).max().getAsInt();
		double sum = 0;
		for (int i = 0; i < n; i++) {
			sum += (double)scores[i] / m * 100;
		}
		bw.write(sum / n + "\n");

		br.close();
		bw.flush();
		bw.close();
	}
}
