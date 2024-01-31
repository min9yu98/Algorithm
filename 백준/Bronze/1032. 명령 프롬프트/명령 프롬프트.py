n = int(input())
files = [input() for _ in range(n)]
result = ''
for i in range(len(files[0])):
    tmp = files[0]
    flag = False
    for j in range(1, n):
        if tmp[i] != files[j][i]:
            flag = True
            result += '?'
            break
    if not flag:
        result += tmp[i]

print(result)
