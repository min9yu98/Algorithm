import sys
import heapq

input = sys.stdin.readline

N = int(input())
left = []
right = []

for i in range(N):
    n = int(input())
    if len(left) == len(right):
        heapq.heappush(left, -n)
    else:
        heapq.heappush(right, n)
    if right and right[0] < -left[0]:
        lv = heapq.heappop(left)
        rv = heapq.heappop(right)
        heapq.heappush(left, -rv)
        heapq.heappush(right, -lv)
    print(-left[0])
