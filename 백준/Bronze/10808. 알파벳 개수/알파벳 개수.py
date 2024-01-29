s = input()
alpha = [0] * 26
for i in s:
    alpha[ord(i) - 97] += 1
print(" ".join(list(map(str, alpha))))
