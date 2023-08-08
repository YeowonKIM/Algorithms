import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    ranking = [list(map(int, input().split())) for _ in range(n)]
    ranking.sort()
    current_top = ranking[0][1]
    pass_num = 1

    for j in range(1, len(ranking)):
        if ranking[j][1] < current_top:
            current_top = ranking[j][1]
            pass_num += 1

    print(pass_num)
