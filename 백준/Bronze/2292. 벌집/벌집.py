n = int(input())
first = 1
limit_max_plus = 6
room = 1
while n > first:
    room += 1
    first += limit_max_plus
    limit_max_plus += 6
print(room)
