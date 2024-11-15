import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k, t, m = map(int, input().split())
    score_dict = {i: {j: 0 for j in range(1, k + 1)} for i in range(1, n + 1)}
    submit_cnt = {i: 0 for i in range(1, n + 1)}
    last_submit = {i: 0 for i in range(1, n + 1)}
    for idx in range(m):
        i, j, s = map(int, input().split())
        score_dict[i][j] = max(score_dict[i][j], s)
        submit_cnt[i] += 1
        last_submit[i] = idx
    score_lst = []
    for idx, scores in score_dict.items():
        score_lst.append([idx, sum(scores.values()), submit_cnt[idx], last_submit[idx]])
    score_lst.sort(key=lambda x: (-x[1], x[2], x[3]))
    for i in range(len(score_lst)):
        if score_lst[i][0] == t:
            print(i + 1)
            break
