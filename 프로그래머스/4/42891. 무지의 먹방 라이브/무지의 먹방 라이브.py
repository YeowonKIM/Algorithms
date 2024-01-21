import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    N = len(food_times)
    prev = 0

    q = []
    for index, time in enumerate(food_times):
        heapq.heappush(q, (time, index+1))

    while k - (q[0][0] - prev) * N >= 0:
        time, curr = heapq.heappop(q)
        k -= (time - prev) * N
        prev = time
        N -= 1

    q.sort(key=lambda x:x[1])
    return q[k % N][1]