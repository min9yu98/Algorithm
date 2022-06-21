a = int(input())
b = int(input())
c = int(input())
arr = list(str(a * b * c))
sen = sorted(set(arr))

num = [0 for i in range(10)]
for i in range(len(sen)):
    num[int(sen[i])] += arr.count(sen[i])

for j in num:
    print(j)
    
