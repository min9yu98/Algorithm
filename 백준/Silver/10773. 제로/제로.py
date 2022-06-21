import sys
lst = []
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if n == 0:
        lst.pop()
        continue
    lst.append(n)
    
print(sum(lst))