hour, minute = map(int, input().split())
time = int(input())
result = minute + time
if result >= 60:
    if hour + result // 60 >= 24:
        print(hour+(result//60) - 24, result % 60)
    else:
        print(hour + (result//60), result % 60)
else:
    print(hour, result)
