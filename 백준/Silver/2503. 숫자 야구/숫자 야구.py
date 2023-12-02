from itertools import permutations

n = int(input())

nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
possible_nums = list(permutations(nums, 3))

for _ in range(n):
    trial, strike, ball = map(int, input().split())
    trial = list(str(trial))
    removal = 0

    for i in range(len(possible_nums)):
        strike_cnt = ball_cnt = 0
        i -= removal
        for j in range(3):
            if possible_nums[i][j] == trial[j]:
                strike_cnt += 1
            elif trial[j] in possible_nums[i]:
                ball_cnt += 1

        if (strike != strike_cnt) or (ball != ball_cnt):
            possible_nums.remove(possible_nums[i])
            removal += 1

print(len(possible_nums))