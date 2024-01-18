def solution(s):
    round = 0
    zero_cnt = 0

    while True:
        if s == "1":
            break
        zero_cnt += s.count("0")
        s = s.replace("0", "")

        s = bin(len(s))[2:]
        round +=1

    return [round, zero_cnt]