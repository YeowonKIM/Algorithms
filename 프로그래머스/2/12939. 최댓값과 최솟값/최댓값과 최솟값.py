def solution(s):
    list_s = list(map(int, s.split()))
    list_s.sort()
    answer = str(list_s[0]) + " " + str(list_s[-1])
    return answer
