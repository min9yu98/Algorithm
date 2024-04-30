import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

s = input().strip()
print("\n".join(sorted([s[i:] for i in range(len(s))])))
