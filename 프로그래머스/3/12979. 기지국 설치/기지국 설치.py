def solution(n, stations, w):
    answer = 0
    stations.sort()
    std = (2 * w) + 1
    tmp = 1
    for station in stations:
        bet = (station - w - tmp) if (station - w - tmp) > 0 else 0
        answer += bet // std + (1 if bet % std else 0)
        tmp = station + w + (1 if station + w + 1 <= n else n)
    answer += (n - stations[-1] - w) // std + (1 if (n - stations[-1] - w) % std else 0)
    return answer