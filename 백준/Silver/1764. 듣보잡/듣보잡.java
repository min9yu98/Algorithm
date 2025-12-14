
import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		Map<String, Boolean> map = new HashMap<>();
		List<String> resultList = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			String name = br.readLine();
			map.put(name, true);
		}

		for (int i = 0; i < M; i++) {
			String name = br.readLine();
			if (map.containsKey(name)) {
				resultList.add(name);
			}
		}

		resultList.sort(String::compareTo);
		System.out.println(resultList.size());
		for (String name : resultList) {
			System.out.println(name);
		}
	}

}