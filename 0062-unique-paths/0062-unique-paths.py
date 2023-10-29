class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(r, c):
            if r==0 and c==0:
                # (0, 0): 1
                memo[(r, c)] = 1
                return memo[(r, c)]

            path_nums = 0
            if (r, c) not in memo:
                if r-1 >= 0:
                    path_nums += dfs(r-1, c)
                if c-1 >= 0:
                    path_nums += dfs(r, c-1)
                memo[(r, c)] = path_nums
            return memo[(r, c)]
        return dfs(m-1, n-1)