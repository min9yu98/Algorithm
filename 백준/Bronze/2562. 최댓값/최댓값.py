li = []
for _ in range(9):
    li.append(int(input()))
print(max(li), li.index(max(li)) + 1, sep = '\n')          
