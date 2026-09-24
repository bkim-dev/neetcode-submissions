class Solution:
    def climbStairs(self, n: int) -> int:
        # can step either n+1 or n+2 distance
        memo = [-1] * n

        def dfs(i):
            if i >= n:
                return i == n
            if memo[i] != -1:
                return memo[i]
            memo[i] = (dfs(i+1) + dfs(i+2))
            return memo[i]

        return dfs(0)