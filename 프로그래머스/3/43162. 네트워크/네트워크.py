def solution(n, computers):

    def dfs(i):
        visited[i] = 1
        for j in range(n):
            if computers[i][j] and not visited[j]:
                dfs(j)

    answer = 0
    visited = [0] * len(computers)
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer