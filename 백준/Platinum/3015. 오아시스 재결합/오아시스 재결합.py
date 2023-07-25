from sys import stdin


def count_num():
    stack = []
    ans = 0

    for h in heights:
        while stack and stack[-1][height] < h:
            ans += stack.pop()[cnt]

        if not stack:
            stack.append((h, 1))
            continue

        if stack[-1][height] == h:
            cnt_same = stack.pop()[cnt]
            ans += cnt_same

            if stack:
                ans += 1
            stack.append((h, cnt_same + 1))

        else:
            stack.append((h, 1))
            ans += 1

    return ans

height, cnt = 0, 1
n = int(stdin.readline())
heights = [int(stdin.readline()) for _ in range(n)]
print(count_num())