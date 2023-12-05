N = int(input())
location = []

for _ in range(N):
    location.append(list(map(int, input().split())))

answer = [1<<30] * (N+1)

for i in range(N):
    for j in range(N):
        mid_x, mid_y = location[i][0], location[j][1]
        distance = []
        for k in range(N):
            distance.append(abs(mid_x - location[k][0]) + abs(mid_y - location[k][1]))
        distance.sort()
        total_distance = 0
        for d in range(N):
            total_distance += distance[d]
            if answer[d] > total_distance:
                answer[d] = total_distance

print(*answer[:N])