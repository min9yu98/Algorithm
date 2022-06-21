a, b = map(int, input().split())
list_a = []
list_b = []
list_su = []
list_go = []
b_mul = 0
# a의 공약수
for a_cf in range(1, a+1):
    if a % a_cf == 0:
        list_a.append(a_cf)

# b의 공약수 
for b_cf in range(1, b+1):
    if b % b_cf == 0:
        list_b.append(b_cf)

# a와 b의 최대공약수
for max_cf in list_a:
    if max_cf in list_b:
        list_su.append(max_cf)
max_list = max(list_su)

# a와 b의 최소공배수
for min_mul in range(1, a+1):
    b_mul = b * min_mul
    if b_mul % a == 0:
        list_go.append(b_mul)
min_list = min(list_go)
print(max_list)
print(min_list)
