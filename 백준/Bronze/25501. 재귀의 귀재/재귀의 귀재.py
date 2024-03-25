import sys

input = sys.stdin.readline


def recur(word, head, rear):
    global cnt
    cnt += 1
    if head >= rear:
        return 1
    elif word[head] != word[rear]:
        return 0
    else:
        return recur(word, head + 1, rear - 1)


def isPalindrome(word):
    return [recur(word, 0, len(word) - 1), cnt]


for _ in range(int(input())):
    s = input().strip()
    cnt = 0
    ans = isPalindrome(s)
    print(ans[0], ans[1])
