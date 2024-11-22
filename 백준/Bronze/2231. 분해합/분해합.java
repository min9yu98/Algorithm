import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int n = Integer.parseInt(br.readLine());

		boolean flag = false;
		for (int i = 1; i <= n; i++) {
			int tmp = 0;
			tmp += i;
			String str = String.valueOf(i);
			tmp += str.chars().map(c -> c - '0').sum();
			if (tmp == n) {
				bw.write(i + "\n");
				flag = true;
				break;
			}
		}

		if (!flag) {
			bw.write(0 + "\n");
		}

		br.close();
		bw.flush();
		bw.close();
	}
}