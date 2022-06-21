import sys
lst = []
for i in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()
    if command[0] == "push": lst.append(int(command[1]))
    elif command[0] == "pop": print(-1 if lst == [] else lst.pop())
    elif command[0] == "size": print(len(lst))
    elif command[0] == "empty": print(1 if lst == [] else 0)
    elif command[0] == "top": print(-1 if lst == [] else lst[-1])