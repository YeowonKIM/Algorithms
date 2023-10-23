class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(r, c):
            if r==0 and c==0:
                memo[(r, c)] = 1
                return memo[(r, c)]

            unique_paths = 0
            if (r, c) not in memo:
                if r-1 >= 0:
                    unique_paths += dfs(r-1, c)
                if c-1 >= 0:
                    unique_paths += dfs(r, c-1)
                memo[(r, c)] = unique_paths
            return memo[(r, c)]
        return dfs(m-1, n-1)
        