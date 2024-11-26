import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		int[] arr = new int[1000001];
		arr[1] = 0;
		arr[2] = 1;
		arr[3] = 1;
		for (int i = 4; i <= n; i++) {
			if (i % 2 == 0 && i % 3 == 0) {
				arr[i] = Math.min(arr[i - 1] + 1, Math.min(arr[i / 2] + 1, arr[i / 3] + 1));
			} else if (i % 2 == 0) {
				arr[i] = Math.min(arr[i - 1] + 1, arr[i / 2] + 1);
			} else if (i % 3 == 0) {
				arr[i] = Math.min(arr[i - 1] + 1, arr[i / 3] + 1);
			} else {
				arr[i] = arr[i - 1] + 1;
			}
		}
		System.out.println(arr[n]);
	}


}
