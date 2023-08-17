h, w, n, m = map(int, input().split())

x = h // (n + 1)
y = w // (m + 1)

if h % (n + 1) != 0:
    x = h // (n + 1) + 1
if w % (m + 1) != 0:
    y = w // (m + 1) + 1

print(x * y)