import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		boolean flag;
		while (true) {
			String num = br.readLine();
			if (num.equals("0")) {
				break;
			}
			flag = false;
			for (int i = 0; i < num.length() / 2; i++) {
				if (num.charAt(i) != num.charAt(num.length() - 1 - i)) {
					flag = true;
					break;
				}
			}
			if (flag) {
				bw.write("no\n");
			} else {
				bw.write("yes\n");
			}
			bw.flush();
		}

		br.close();
		bw.flush();
		bw.close();
	}
}