x = list(input())
arr = sorted(set(x))
result = [-1 for i in range(26)]
for i in range(len(arr)):
    result[ord(x[x.index(arr[i])]) - 97] += x.index(arr[i]) + 1
for j in result:
    print(j, end = ' ')
