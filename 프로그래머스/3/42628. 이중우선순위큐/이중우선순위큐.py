import heapq

def solution(operations):
    min_heap = []

    for o in operations:
        if o[0] == 'I':
            heapq.heappush(min_heap, int(o[2:]))
        else:
            if not min_heap:
                continue
            if o[2] == '1':
                min_heap.pop(-1)
                # min_heap = heapq.nlargest(len(min_heap), min_heap)[1:]
                # heapq.heapify(min_heap)
            elif o[3] =='1':
                heapq.heappop(min_heap)

    if not min_heap:
        return [0, 0]
    else:
        return [max(min_heap), min(min_heap)]