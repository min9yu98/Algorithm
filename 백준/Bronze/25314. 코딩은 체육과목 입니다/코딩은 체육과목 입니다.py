import sys
_input = sys.stdin.readline

n = int(int(_input()) / 4)

result = ['long' for _ in range(n)]
result.append('int')
print(' '.join(result))
