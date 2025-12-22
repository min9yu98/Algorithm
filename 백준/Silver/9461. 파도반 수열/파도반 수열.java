
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		long[] arr = new long[101];
		arr[0] = 1;
		arr[1] = 1;
		arr[2] = 1;
		for (int i = 3; i < 101; i++) {
			arr[i] = arr[i - 2] + arr[i - 3];
		}
		int T = Integer.parseInt(br.readLine());
		for (int ord = 0; ord < T; ord++) {
			int N = Integer.parseInt(br.readLine());
			System.out.println(arr[N - 1]);
		}
	}
}