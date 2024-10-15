def isSame(stand, word):
    return sum(1 for s, w in zip(stand, word) if s == w) == len(stand) - 1

def dfs(begin, target, cnt, visited, words):
    if begin == target:
        return cnt
    result = 51
    for i in range(len(words)):
        if not visited[i]:
            if isSame(begin, words[i]):
                visited[i] = True
                result = min(result, dfs(words[i], target, cnt + 1, visited, words))
                visited[i] = False
    return result

def solution(begin, target, words):
    answer = dfs(begin, target, 0, [False for i in range(len(words))], words)
    return answer if answer != 51 else 0
