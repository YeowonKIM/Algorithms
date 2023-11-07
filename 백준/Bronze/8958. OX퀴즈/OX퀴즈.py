n = int(input())
for i in range(n):
    a = input()
    a = list(a)
    sum = 0
    cnt = 0
    for x in a:
        if x == "O":
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    print(sum)