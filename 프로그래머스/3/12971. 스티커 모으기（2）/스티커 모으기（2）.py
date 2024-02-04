def solution(sticker):
    N = len(sticker)
    if N == 1:
        return sticker[0]

    # 첫번째 스티커 선택
    dp1 = [0] + sticker[:-1]
    for i in range(2, N):
        dp1[i] = max(dp1[i-1], dp1[i-2]+dp1[i])

    # 두번째 스티커 선택
    dp2 = [0] + sticker[1:]
    for i in range(2, N):
        dp2[i] = max(dp2[i-1], dp2[i-2]+dp2[i])

    return max(dp1[-1], dp2[-1])