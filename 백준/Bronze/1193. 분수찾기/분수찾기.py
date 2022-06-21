n = int(input())
child = []
parent = []
def check(n):
    a = 0
    for i in range(1, n + 1):
        a += i
        if a >= n:
            break
    return i + 1, a
check = check(n)
if check[0] % 2 == 0:
    for i in range(1, check[0]):
        child.append(check[0] - i)
        parent.append(i)
else:  
    for i in range(1, check[0]):
        parent.append(check[0] - i)
        child.append(i)
print(child[n - check[1] - 1], '/', parent[n - check[1] - 1], sep = '')