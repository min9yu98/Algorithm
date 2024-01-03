import sys
_input = sys.stdin.readline

for _ in range(int(_input())):
    n, m = map(int, _input().split())
    queue = list(map(int, _input().split()))
    weight = queue[m]
    weight_list = list(reversed(sorted(queue)))
    loc = [0 for _ in range(n)]
    loc[m] = 1
    cnt = 0
    while 1 in loc:
        if weight_list[0] != queue[0]:
            queue.append(queue[0])
            queue.pop(0)
            loc.append(loc[0])
            loc.pop(0)
        else:
            weight_list.pop(0)
            queue.pop(0)
            loc.pop(0)
            cnt += 1
    print(cnt)
