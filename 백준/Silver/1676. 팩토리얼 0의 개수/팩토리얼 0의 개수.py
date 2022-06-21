n = int(input())
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)
num = list(str(fact(n)))
lst = []
for i in range(len(num)):
    lst.append(int(num[len(num) - i - 1]))
cnt = 0
for i in lst:
    if i == 0:
        cnt += 1
    else:
        break
print(cnt)
