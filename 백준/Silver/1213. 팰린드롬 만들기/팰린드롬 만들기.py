import sys
from collections import Counter
input = sys.stdin.readline

s = list(input().strip())
s_type = Counter(s)
check = 0
mid = ''
for k, v in s_type.items():
    if v % 2 != 0:
        check += 1
        mid = k
        if check > 1:
            print("I'm Sorry Hansoo")
            exit()
result = ''
for k, v in sorted(s_type.items()):
    result += (k * (v // 2))
print(result + mid + result[::-1])
