def prime(n):
  if n == 1:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True

all = list(range(2, 246912))
memo = []

for i in all:
  if prime(i):
    memo.append(i)

while True:
  n = int(input())
  cnt = 0
  if n == 0:
    break
  for i in memo:
    if n < i <= 2 * n:
      cnt += 1
  print(cnt)