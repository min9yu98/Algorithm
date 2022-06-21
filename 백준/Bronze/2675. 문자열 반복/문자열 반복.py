for _ in range(int(input())):
    n, s = input().split()
    arr = []
    result = ''
    
    for i in list(s):
        arr.append(i * int(n))
        
    for j in range(len(arr)):
        result += arr[j]
    print(result)
    
