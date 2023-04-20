import sys
# input = sys.stdin.readline
# print = sys.stdout.write

word = list(map(str, sys.stdin.readline().rstrip("\n")))
result = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        w1 = word[:i]
        w2 = word[i:j]
        w3 = word[j:]

        w1.reverse()
        w2.reverse()
        w3.reverse()

        result.append("".join(w1 + w2 + w3))

print(min(result))