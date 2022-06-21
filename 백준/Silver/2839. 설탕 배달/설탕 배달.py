sugar = int(input())
box = 0

while True:
    if sugar % 5 == 0:
        box = box + sugar//5
        print(box)
        break
    sugar -= 3
    box += 1
    if sugar < 0:
        print(-1)
        break
    
