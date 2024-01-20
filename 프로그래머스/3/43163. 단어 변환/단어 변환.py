from collections import deque

def solution(begin, target, words):
    answer = 0
    N = len(words)
    visited = [False for _ in range(N)]

    q = deque()
    q.append((begin, 0))
    while q:
        word, depth = q.popleft()
        if word == target:
            answer = depth
            break
        for i in range(N):
            dup_cnt = 0
            if not visited[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        dup_cnt += 1
                if dup_cnt == 1:
                    q.append((words[i], depth+1))
                    visited[i] = True

    return answer