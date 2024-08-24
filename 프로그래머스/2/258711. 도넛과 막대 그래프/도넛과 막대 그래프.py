def solution(edges):
    dic = {}
    for node1, node2 in edges:
        if not dic.get(node1):
            dic[node1] = [0, 0]
        if not dic.get(node2):
            dic[node2] = [0, 0]
        dic[node1][0] += 1
        dic[node2][1] += 1
    answer = [0, 0, 0, 0]
    for key, counts in dic.items():
        if counts[0] >= 2 and counts[1] == 0:
            answer[0] = key
        elif counts[0] == 0 and counts[1] > 0:
            answer[2] += 1
        elif counts[0] >= 2 and counts[1] >= 2:
            answer[3] += 1
    answer[1] = dic[answer[0]][0] - answer[2] - answer[3]

    return answer