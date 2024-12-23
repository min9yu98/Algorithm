import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int H = Integer.parseInt(st.nextToken());
		int W = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int tmp_h, tmp_w;
		if (H % (N + 1) != 0) {
			tmp_h = H / (N + 1) + 1;
		} else {
			tmp_h = H / (N + 1);
		}
		if (W % (M + 1) != 0) {
			tmp_w = W / (M + 1) + 1;
		} else {
			tmp_w = W / (M + 1);
		}
		System.out.println(tmp_h * tmp_w);
	}
}