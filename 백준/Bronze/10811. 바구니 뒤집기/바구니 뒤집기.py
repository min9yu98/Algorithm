n, m = map(int, input().split())
basket = [i for i in range(1, n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    basket[a - 1:b] = reversed(basket[a - 1:b])
print(' '.join(list(map(str, basket))))
