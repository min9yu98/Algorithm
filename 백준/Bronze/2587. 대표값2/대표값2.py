numbers = [int(input()) for _ in range(5)]
print(int(sum(numbers)/len(numbers)))
numbers.sort()
print(numbers[2])
