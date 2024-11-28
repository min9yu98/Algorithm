import java.io.*;

public class Main {

	static int[] zero = new int[41];
	static int[] one = new int[41];

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		zero[0] = 1;
		one[0] = 0;
		zero[1] = 0;
		one[1] = 1;
		for (int i = 2; i < 41; i++) {
			zero[i] = zero[i - 1] + zero[i - 2];
			one[i] = one[i - 1] + one[i - 2];
		}
		int test = Integer.parseInt(br.readLine());
		for (int t = 0; t < test; t++) {
			int n = Integer.parseInt(br.readLine());
			bw.write(zero[n] + " " + one[n] + "\n");
		}
		br.close();
		bw.flush();
		bw.close();
	}

}
