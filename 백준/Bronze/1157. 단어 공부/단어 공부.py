x = input().upper()
arr = sorted(list(set(x)))
c = []
for i in range(len(arr)):
    c.append(x.count(arr[i]))
if c.count(max(c)) > 1:
    print('?')
else:
    print(arr[c.index(max(c))])
