import sys

ax, ay, bx, by, cx, cy = map(int, sys.stdin.readline().split())

if (ax - bx) * (cy - ay) == (cx - ax) * (ay - by):
    print(-1.0)
    exit(0)

ab = ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5
bc = ((cx - bx) ** 2 + (cy - by) ** 2) ** 0.5
ca = ((ax - cx) ** 2 + (ay - cy) ** 2) ** 0.5

lst = [ab + bc, bc + ca, ca + ab]

result = max(lst) - min(lst)

print(result * 2)

