first = int(input())
end = int(input())

def check(n):
    lst = []
    for i in range(1, n + 1):
        if n % i == 0:
            lst.append(i)
    return lst
hap = 0
mini = []
for i in range(first, end + 1):
    n = check(i)
    if len(n) == 2:
        hap += n[-1]
        mini.append(n[-1])
        
if mini == []:
    print(-1)
else:
    print(hap)
    print(min(mini))

                
