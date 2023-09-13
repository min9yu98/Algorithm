import heapq

heap = []
n = int(input())
for _ in range(n):
    lst = list(map(int, input().split()))
    for e in lst:
        if len(heap) < n:
            heapq.heappush(heap, e)
        else:
            if heap[0] < e:
                heapq.heappop(heap)
                heapq.heappush(heap, e)
print(heap[0])
