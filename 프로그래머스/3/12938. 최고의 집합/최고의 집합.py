def solution(n, s):
    div = s // n
    mod = s % n
    answer = [div] * n
    for i in range(mod):
        answer[i] += 1
    if n > s:
        return [-1]
    else:
        return sorted(answer)