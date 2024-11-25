import java.io.*;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int t = Integer.parseInt(br.readLine());
		int[][] arr = new int[15][15];
		for (int i = 1; i < 15; i++) {
			arr[0][i] = i;
		}
		int tmp = 0;
		for (int i = 1; i < 15; i++) {
			for (int j = 1; j < 15; j++) {
				for (int k = 1; k <= j; k++) {
					tmp += arr[i - 1][k];
				}
				arr[i][j] = tmp;
				tmp = 0;
			}
		}

		for (int z = 0; z < t; z++) {
			int k = Integer.parseInt(br.readLine());
			int n = Integer.parseInt(br.readLine());
			System.out.println(arr[k][n]);
		}
	}
}