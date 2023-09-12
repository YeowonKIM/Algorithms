import sys

input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))

num = 0
nums_sum = [0]
for i in seq:
    num += i
    nums_sum.append(num)


def function(st, ed, nums_sum):
    return nums_sum[ed] - nums_sum[st - 1]


for _ in range(m):
    a, b = map(int, input().split())
    print(function(a, b, nums_sum))