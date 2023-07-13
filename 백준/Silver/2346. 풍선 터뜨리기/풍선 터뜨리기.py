import sys
from collections import deque

n = int(input())
balloons = deque(enumerate(map(int, input().split())))

while balloons:
    idx, num = balloons.popleft()
    print(idx+1, end=" ")
    
    if num > 0:
        balloons.rotate(-(num-1))
    elif num < 0:
        balloons.rotate(-num)