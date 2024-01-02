A, B = map(int, input().split())

def count_square2(num):
    cnt = 0
    cnt += num
    for i in range(1, 99):
        cnt += (num//(2**i))*((2**i)-(2**(i-1)))
    return cnt


cnt_A = count_square2(A-1)
cnt_B = count_square2(B)
print(cnt_B - cnt_A)
