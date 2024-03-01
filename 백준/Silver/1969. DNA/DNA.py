import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dna = [input().strip() for _ in range(n)]
dna_dic = {0: 'A', 1: 'G', 2: 'T', 3: 'C'}
ans_dna = [[] for _ in range(m)]
hamming_dna = ''
diff_cnt = 0
for i in range(m):
    lst = [0, 0, 0, 0]
    for j in range(n):
        if dna[j][i] == 'A':
            lst[0] += 1
        elif dna[j][i] == 'G':
            lst[1] += 1
        elif dna[j][i] == 'T':
            lst[2] += 1
        else:
            lst[3] += 1
    for k in range(4):
        if lst[k] == max(lst):
            ans_dna[i].append(dna_dic[k])
for i in range(m):
    ans_dna[i].sort()
    hamming_dna += ans_dna[i][0]
    for j in range(n):
        if dna[j][i] != ans_dna[i][0]:
            diff_cnt += 1
print(hamming_dna)
print(diff_cnt)
