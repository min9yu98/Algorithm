import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

laser = input().strip()
laser = laser.replace("()", "!")
cnt = 0
push_cnt = 0
pop_cnt = 0
for i in range(len(laser)):
    if laser[i] == '(':
        push_cnt += 1
    elif laser[i] == '!':
        cnt += push_cnt
        if pop_cnt != 0:
            push_cnt -= pop_cnt
            pop_cnt = 0
    else:
        pop_cnt += 1
if pop_cnt != 0:
    cnt += push_cnt
print(cnt)
