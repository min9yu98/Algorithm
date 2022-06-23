def draw_stars(n):
  if n == 1:
    return ['*']
  
  stars = draw_stars(n // 3)
  lst = []

  for s in stars:
    lst.append(s * 3)
  for s in stars:
    lst.append(s + ' ' * (n // 3) + s)
  for s in stars:
    lst.append(s * 3)

  return lst

n = int(input())
print('\n'.join(draw_stars(n)))