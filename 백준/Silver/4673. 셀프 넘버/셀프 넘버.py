# 생성자있는 셀프넘버 출력함수
def d(n):
    result_st = str(n)
    result = n
    for i in range(len(result_st)):
        result += int(result_st[i])
    return result

list_d = []
for i in range(1, 10001):
    list_d.append(d(i))

for j in range(1, 10001):
    if j not in list_d:
        print(j)
