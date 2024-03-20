import sys

input = sys.stdin.readline

laser = input().strip()
laser = laser.replace("()", "!")
stack = []
cnt = 0
pop_cnt = 0
for i in range(len(laser)):
    if laser[i] == '(':
        stack.append(laser[i])
    elif laser[i] == '!':
        cnt += len(stack)
        if pop_cnt != 0:
            for _ in range(pop_cnt):
                stack.pop()
            pop_cnt = 0
    else:
        pop_cnt += 1
if pop_cnt != 0:
    cnt += len(stack)
print(cnt)
