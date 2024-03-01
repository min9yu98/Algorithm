import sys
input = sys.stdin.readline

n = int(input())
first = list(map(int, input().split()))
second = list(map(int, input().split()))
print(sum(list(map(lambda x: abs(x), first))) + sum(list(map(lambda x: abs(x), second))))
