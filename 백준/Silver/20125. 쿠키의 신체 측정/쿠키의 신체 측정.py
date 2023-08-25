n = int(input())
body = []

for _ in range(n):
    s = input()
    body.append(s)

head = False
arm = False
belly = False
leg = False
left_arm, right_arm, stomach, left_leg, right_leg = 0, 0, 0, 0, 0
x, y = 0, 0 # 머리 (x, y) 좌표
for i in range(n):
    if body[i].count('*') == 1 and not head:
        head = True
        for j in range(n):
            if body[i][j] == '*':
                x, y = j, i
                break
        continue
    if head and not arm:
        arm = True
        for j in range(n):
            if body[i][j] == '*':
                if j < x:
                    left_arm += 1
                elif j > x:
                    right_arm += 1
                else:
                    continue
        continue
    if head and arm and not leg:
        if body[i].count("*") == 1:
            stomach += 1
            belly = True
        else:
            leg = True
    if head and arm and belly and leg:
        if body[i].count("*") == 2:
            left_leg += 1
            right_leg += 1
        elif body[i].count("*") == 1:
            for j in range(n):
                if body[i][j] == '*':
                    if j < x:
                        left_leg += 1
                    elif j > x:
                        right_leg += 1
                    break

print(y + 2, x + 1)
print(left_arm, right_arm, stomach, left_leg, right_leg)