import heapq
import sys

heap = []
for _ in range(int(sys.stdin.readline().rstrip())):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if not heap:
            print(0)
            continue
        print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)

