import sys
lst = []
for i in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()
    if command[0] == "push_front": lst.insert(0, int(command[1]))
    elif command[0] == "push_back": lst.append(int(command[1]))
    elif command[0] == "pop_front":
        if lst == []: print(-1)
        else: print(lst[0]); lst.remove(lst[0])
    elif command[0] == "pop_back":
        if lst == []: print(-1)
        else: print(lst.pop())
    elif command[0] == "size": print(len(lst))
    elif command[0] == "empty": print(1 if lst == [] else 0)
    elif command[0] == "front": print(-1 if lst == [] else lst[0])
    elif command[0] == "back": print(-1 if lst ==[] else lst[-1])
