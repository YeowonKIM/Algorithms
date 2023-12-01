n = int(input())

for _ in range(n):
    input_num = int(input())
    check = True

    for i in range(2, 1000000):
        if input_num % i ==0:
            check = False
            break

    if check:
        print("YES")
    else:
        print("NO")