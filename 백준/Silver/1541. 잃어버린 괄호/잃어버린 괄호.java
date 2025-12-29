
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int result = Integer.MAX_VALUE;
		String exp = br.readLine();
		String[] spl = exp.split("-");
		for (int i = 0; i < spl.length; i++) {
			int tmp = 0;
			String[] sumSpl = spl[i].split("\\+");
			for (int j = 0; j < sumSpl.length; j++) {
				tmp += Integer.parseInt(sumSpl[j]);
			}

			if (result == Integer.MAX_VALUE) {
				result = tmp;
			} else {
				result -= tmp;
			}
		}
		System.out.println(result);
	}

}