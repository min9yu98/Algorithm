word = []
for _ in range(int(input())):
    word.append(input())
for i in sorted(sorted(set(word)), key = lambda e: len(e)):
    print(i)
