def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if [x, y] in puddles:
                continue
            r1 = dp[y - 1][x]
            r2 = dp[y][x - 1]
            if [x, y - 1] in puddles:
                r1 = 0
            if [x - 1, y] in puddles:
                r2 = 0
            dp[y][x] += r1 + r2
    return dp[n][m] % 1000000007
