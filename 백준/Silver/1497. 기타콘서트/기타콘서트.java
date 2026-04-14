
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		long[] guitarList = new long[N];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			String guitar = st.nextToken();
			String song = st.nextToken();

			long sub = 0L;
			for (int j = 0; j < M; j++) {
				if (song.charAt(j) == 'Y') {
					sub |= (1L << j);
				}
			}
			guitarList[i] = sub;
		}

		int minGuitar = Integer.MAX_VALUE;
		int maxSong = 0;
		for (int i = 1; i < (1 << N); i++) {
			long song = 0L;
			int guitarCnt = 0;

			for (int j = 0; j < N; j++) {
				if ((i & (1 << j)) != 0) {
					guitarCnt++;
					song |= guitarList[j];
				}
			}

			int songCnt = Long.bitCount(song);

			if (songCnt > maxSong) {
				maxSong = songCnt;
				minGuitar = guitarCnt;
			} else if (songCnt == maxSong) {
				minGuitar = Math.min(minGuitar, guitarCnt);
			}
		}

		if (maxSong == 0) {
			System.out.println(-1);
		} else {
			System.out.println(minGuitar);
		}
	}

}
