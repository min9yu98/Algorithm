import sys
import heapq

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
set_nums = list(set(nums))
set_nums.sort(reverse=True)
check_dic = {x: 0 for x in set_nums}
for i in range(len(set_nums)):
    check_dic[set_nums[i]] = len(set_nums) - i - 1
for e in nums:
    print(check_dic[e], end=" ")
