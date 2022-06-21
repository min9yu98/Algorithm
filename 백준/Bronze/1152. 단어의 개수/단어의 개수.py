sen = input().strip(' ').split()
d = sen.count(' ')
for i in range(d):
    del sen[sen.index(' ')]

print(len(sen))
