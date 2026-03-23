import java.util.stream.LongStream;

class Solution {
    public int[] solution(int n, long left, long right) {
        return LongStream.rangeClosed(left, right)
            .mapToInt(i -> (int) Math.max(i / n, i % n) + 1)
            .toArray();
    }
}

// 1234 > 1234223433344444
// 2234
// 3334
// 4444

// left % n = 2, right / n = 0 > 3
// right % n = 2, rigth / n = 1 223
// 12345
// 22345
// 33345
// 44445
// 55555