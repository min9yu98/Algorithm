
import java.io.*;
import java.util.*;

class Person {
	int age;
	String name;
	int order;

	public Person(int age, String name, int order) {
		this.age = age;
		this.name = name;
		this.order = order;
	}
}

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		List<Person> people = new ArrayList<>();
		int N = Integer.parseInt(st.nextToken());
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			int age = Integer.parseInt(st.nextToken());
			String name = st.nextToken();
			people.add(new Person(age, name, i));
		}

		people.sort((p1, p2) -> {
			if (p1.age != p2.age) {
				return Integer.compare(p1.age, p2.age);
			}
			return Integer.compare(p1.order, p2.order);
		});

		StringBuilder sb = new StringBuilder();
		for (Person person : people) {
			sb.append(person.age).append(" ").append(person.name).append("\n");
		}
		System.out.println(sb);
	}
}