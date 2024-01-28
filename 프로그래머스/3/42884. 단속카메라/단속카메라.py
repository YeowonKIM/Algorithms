def solution(routes):
    answer = 1
    N = len(routes)
    routes.sort(key=lambda x:x[1])

    camera = routes[0][1]
    for i in range(1, len(routes)):
        if routes[i][0] > camera:
            camera = routes[i][1]
            answer += 1

    return answer