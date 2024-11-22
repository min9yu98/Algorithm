import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		long n = Long.parseLong(br.readLine());

		for (int i = 1; i < 1000000; i++) {
			if (n == 1) {
				bw.write("1" + "\n");
				break;
			}
			if (3L * i * i - 3 * i + 2 > n) {
				bw.write(i + "\n");
				break;
			}
		}

		br.close();
		bw.flush();
		bw.close();
	}
}