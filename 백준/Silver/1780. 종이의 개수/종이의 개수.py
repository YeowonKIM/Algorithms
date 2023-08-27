from sys import stdin

# 입력받기
n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int, stdin.readline().split())))

# 종이 숫자별 개수 결과
result = {-1:0, 0:0, 1:0}

# 종이 숫자가 다르면 분할
def divide(row, col, n):
    curr_num = paper[row][col]

    for i in range(row, row+n):
        for j in range(col, col+n):
            # 현재 기순인 종이 숫자와 다르면 1/3씩 분할
            if paper[i][j] != curr_num:
                next = n // 3
                divide(row, col, next)
                divide(row, col+next, next)
                divide(row, col+(next*2), next)
                divide(row+next, col, next)
                divide(row+next, col+next, next)
                divide(row+next, col+(next*2), next)
                divide(row+(next*2), col, next)
                divide(row+(next * 2), col+next, next)
                divide(row+(next * 2), col+(next*2), next)
                return

    result[curr_num] += 1
    return

divide(0,0,n)
for i in result.values():
    print(i)
    