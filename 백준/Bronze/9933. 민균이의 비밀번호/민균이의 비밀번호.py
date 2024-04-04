import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
words = []
for _ in range(n):
    word = list(input().strip())
    words.append(''.join(word))
    if f'{"".join(list(reversed(word)))}' in words:
        print(len(word), word[len(word) // 2])
