import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String word = br.readLine();
		HashMap<Character, Integer> map = new HashMap<>();
		for (int i = 0; i < word.length(); i++) {
			char c = Character.toUpperCase(word.charAt(i));
			if (map.containsKey(c)) {
				map.put(c, map.get(c) + 1);
			} else {
				map.put(c, 1);
			}
		}
		List<Character> keySet = new ArrayList<>(map.keySet());
		keySet.sort((o1, o2) -> map.get(o2).compareTo(map.get(o1)));
		int max = 0;
		char result = '?';
		for (Character key: keySet) {
			if (map.get(key) > max) {
				max = map.get(key);
				result = key;
			} else if (map.get(key) == max) {
				result = '?';
			}
		}
		System.out.println(result);
	}
}