def solution(s):
    s = s.split(' ')  
    s = [i.capitalize() for i in s]
    answer = ' '.join(s)
    return answer
