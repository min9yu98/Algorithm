def hanoi(n, start, aux, goal): # 시작 지점, 보조 지점, 목표지점
  if n == 1:
    print(start, goal)
    return
  hanoi(n - 1, start, goal, aux)
  print(start, goal)
  hanoi(n - 1, aux, start, goal)


n = int(input())

print(2 ** n - 1)
hanoi(n, 1, 2, 3)
