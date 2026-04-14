
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {
		StringBuilder sb = new StringBuilder();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int M = Integer.parseInt(br.readLine());
		int mask = 0;
		for (int i = 0; i < M; i++) {
			String str = br.readLine();

			if ("all".equals(str)) {
				mask = (1 << 21) - 2;
				continue;
			} else if ("empty".equals(str)) {
				mask = 0;
				continue;
			}

			StringTokenizer st = new StringTokenizer(str);
			String comm = st.nextToken();
			int num = Integer.parseInt(st.nextToken());
			if ("add".equals(comm)) {
				mask |= (1 << num);
			} else if ("remove".equals(comm)) {
				mask &= ~(1 << num);
			} else if ("check".equals(comm)) {
				boolean flag;
				sb.append((mask & (1 << num)) != 0 ? 1 : 0).append('\n');
			} else if ("toggle".equals(comm)) {
				if ((mask & (1 << num)) != 0) {
					mask &= ~(1 << num);
				} else {
					mask |= (1 << num);
				}
			}
		}
		System.out.println(sb);
	}

}

