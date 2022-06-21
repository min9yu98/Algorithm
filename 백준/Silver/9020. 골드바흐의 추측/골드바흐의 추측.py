prime = [0 for _ in range(10001)]
prime[1] = 1

for i in range(2, 98):
  for j in range(i * 2, 10001, i):
    prime[j] = 1

for _ in range(int(input())):
  a = int(input())
  b = a // 2

  for i in range(b, 1, -1):
    if prime[a - i] == 0 and prime[i] == 0:
      print(i, a - i)
      break