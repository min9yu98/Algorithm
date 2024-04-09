import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
ans = []
queue = deque([i for i in range(1, n + 1)])
queue.rotate(-k + 1)
while queue:
    ans.append(str(queue[0]))
    queue.popleft()
    queue.rotate(-k + 1)
print('<'+', '.join(ans)+'>')
