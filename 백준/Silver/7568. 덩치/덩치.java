
import java.io.*;
import java.util.*;

class Person {
	int weight;
	int height;

	public Person(int weight, int height) {
		this.weight = weight;
		this.height = height;
	}
}

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		List<Person> people = new ArrayList<>();
		int N = Integer.parseInt(st.nextToken());
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int weight = Integer.parseInt(st.nextToken());
			int height = Integer.parseInt(st.nextToken());
			people.add(new Person(weight, height));
		}

		StringBuilder sb = new StringBuilder();

		for (int i = 0; i < N; i++) {
			int rank = 1;
			for (int j = 0; j < N; j++) {
				if (i == j) continue;
				if (people.get(i).weight < people.get(j).weight && people.get(i).height < people.get(j).height) {
					rank++;
				}
			}
			sb.append(rank).append(" ");
		}
		System.out.println(sb);
	}
}