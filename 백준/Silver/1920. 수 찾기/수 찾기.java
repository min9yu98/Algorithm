
import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		String nums = br.readLine();
		String[] tmpArrNums = nums.split(" ");
		Map<String, Boolean> map = new HashMap<>();
		for (int i = 0; i < N; i++) {
			tmpArrNums[i] = tmpArrNums[i].trim();
			map.put(tmpArrNums[i], true);
		}

		int M = Integer.parseInt(br.readLine());
		String nums2 = br.readLine();
		String[] tmpArrNums2 = nums2.split(" ");
		for (int i = 0; i < M; i++) {
			tmpArrNums2[i] = tmpArrNums2[i].trim();
			if (map.containsKey(tmpArrNums2[i])) {
				System.out.println(1);
			} else {
				System.out.println(0);
			}
		}
	}
}