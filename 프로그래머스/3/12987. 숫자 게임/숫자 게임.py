def solution(A, B):
    A.sort()
    B.sort()
    idx = 0
    for b in B:
        if A[idx] < b:
            idx += 1
    return idx