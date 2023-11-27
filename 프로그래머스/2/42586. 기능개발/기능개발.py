def solution(progresses, speeds):
    cnt = 0
    time = 0
    result = []

    while len(progresses) > 0:
        if progresses[0] + speeds[0] * time >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt:
                result.append(cnt)
                cnt = 0
            time += 1
    result.append(cnt)
    return result