for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    same_score = [0] * 201  # 같은 점수가 있을 경우 5번째 주자의 등수 저장
    score = [0] * 201
    person = [0] * 201  # 총 몇명 들어왔는지 (6명 이상의 주자가 경기에 참여 했는지 판단)
    person_score = [0] * 201  # 상위 4명 체크를 위한 리스트
    for i in range(n):
        person[lst[i]] += 1
        if person[lst[i]] == 5:
            same_score[lst[i]] = i

    sc = 1
    for i in range(n):
        if person[lst[i]] >= 6:
            if person_score[lst[i]] < 4:
                score[lst[i]] += sc
                person_score[lst[i]] += 1
            sc += 1

    winner_score = 1001
    winner = 0
    for i in range(n):
        if person[lst[i]] >= 6 and score[lst[i]] != 0:
            if score[lst[i]] > winner_score:
                continue
            elif score[lst[i]] < winner_score:
                winner_score = score[lst[i]]
                winner = lst[i]
            else:
                if same_score[winner] > same_score[lst[i]]:
                    winner = lst[i]
    print(winner)