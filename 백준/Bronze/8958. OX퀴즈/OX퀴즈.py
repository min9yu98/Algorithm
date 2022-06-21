for _ in range(int(input())):
    test = list(input())
    cnt = 0
    result = 0
    for i in range(len(test)):
        if test[i] == 'O':
            cnt += 1        
        elif test[i] == 'X':
            cnt = 0
        result += cnt
    print(result)
