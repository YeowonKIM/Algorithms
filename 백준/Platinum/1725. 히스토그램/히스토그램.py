import sys
input = sys.stdin.readline

N = int(input())
list = [int(input()) for _ in range(N)]

stack = []
max_area = 0
for i in range(N):
    idx = i
    while stack and stack[-1][1] > list[i]:
        idx, height = stack.pop()
        area = (i-idx) * height
        max_area = max(max_area, area)
    stack.append([idx, list[i]])

while stack:
    idx, height = stack.pop()
    area = (N - idx) * height
    max_area = max(max_area, area)

print(max_area)