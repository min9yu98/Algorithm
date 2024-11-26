import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int t = Integer.parseInt(br.readLine());
		int[] arr = new int[12];
		arr[1] = 1;
		arr[2] = 2;
		arr[3] = 4;
		for (int z = 0; z < t; z++) {
			int n = Integer.parseInt(br.readLine());
			for (int i = 4; i <= n; i++) {
				arr[i] = arr[i - 3] + arr[i - 2] + arr[i - 1];
			}
			System.out.println(arr[n]);
		}
	}
}
