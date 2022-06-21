for _ in range(int(input())):
    floor = int(input())
    num = int(input())
    people = [i for i in range(1, num + 1)]

    for _ in range(floor):
        for e in range(1, num):
            people[e] += people[e - 1]
    print(people[-1])
