n = int(input())
point = sorted(list(map(int, input().split())), reverse = True)
result = 0
for i in range(len(point)):
    result = result + (point[i]/point[0] * 100)
print(result / n)
