import sys
for _ in range(int(sys.stdin.readline())):
    string = list(sys.stdin.readline())
    check = 0
    for i in string:
        if i == "(":
            check += 1
        elif i == ")":
            check -= 1
        if check < 0:
            print("NO")
            break
    if check > 0:
        print("NO")
    elif check == 0:
        print("YES")
    
