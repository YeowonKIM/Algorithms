import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0

    works = [-w for w in works]
    heapq.heapify(works)
    
    while n>0:
        hour = heapq.heappop(works)
        hour += 1
        heapq.heappush(works, hour)
        n-=1
    
    answer = [ w**2 for w in works ]
    
    return sum(answer)