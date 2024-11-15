import sys
import heapq

input = sys.stdin.readline

lst = []
heapq.heapify(lst)
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        if lst:
            print(heapq.heappop(lst))
        else:
            print(0)
    else:
        heapq.heappush(lst, n)
