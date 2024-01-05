def solution(s):
    list_s = list(s.split(' '))
    s_capitalize = [i.capitalize() for i in list_s]
    answer = ' '.join(s_capitalize)
    return answer