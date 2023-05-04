n = int(input())
seat = input()

print(min(n, seat.count("LL") + seat.count("S") + 1))

