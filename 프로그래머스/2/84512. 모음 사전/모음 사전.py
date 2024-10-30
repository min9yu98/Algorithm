def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    global answer
    answer = 0

    def dfs(s):
        global answer
        answer += 1
        if s == word:
            return True
        if len(s) == 5:
            return False
        for al in alpha:
            if dfs(s + al):
                return True
    for al in alpha:
        if dfs(al):
            return answer

