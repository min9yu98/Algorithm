import sys
input = sys.stdin.readline


def sum_lst(lst, idx):
    total = 0
    for element in lst[idx]:
        if element:
            total += max(element)
    return total


def count_q(lst, idx):
    cnt = 0
    for element in lst[idx]:
        if element:
            cnt += len(element)
    return cnt


for _ in range(int(input())):
    n, k, t, m = map(int, input().split())  # n: 팀수, k: 문제 수, t: 나의 팀 id, m: 로그 엔트리 수
    check_q = [[0] * (k + 1) for _ in range(n + 1)]
    score_lst = [[[] for _ in range(k + 1)] for _ in range(n + 1)]
    submit_rank = [0] * (n + 1)
    teams = [[0, 0, 0, 0]]
    for idx in range(m):
        i, j, s = map(int, input().split())
        check_q[i][j] = 1
        score_lst[i][j].append(s)
        submit_rank[i] = idx + 1
    for i in range(1, n + 1):
        total_score = sum_lst(score_lst, i)
        total_solved_q = count_q(score_lst, i)
        last_submit = submit_rank[i]
        teams.append([i, total_score, total_solved_q, last_submit])
    teams.sort(key=lambda x: (-x[1], x[2], x[3]))

    for i in range(n):
        if teams[i][0] == t:
            print(i + 1)
            break
