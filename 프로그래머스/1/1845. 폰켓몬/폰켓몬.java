import java.util.Set;
import java.util.HashSet;

class Solution {
    public int solution(int[] nums) {
        Set<Integer> s = new HashSet<>();
        for (int n: nums) {
            s.add(n);
        }
        int totalLength = nums.length;
        int distinctLength = s.size();
        return Math.min((int) totalLength / 2, distinctLength);
    }
}