student = []
for _ in range(int(input())):
    student.append(list(map(int, input().split())))
for i in student:
    rank = 1
    for j in student:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")


