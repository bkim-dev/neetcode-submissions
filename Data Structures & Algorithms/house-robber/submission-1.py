class Solution:
    def rob(self, nums: List[int]) -> int:
        # starting at i = 1
        # check to rob or not rob a house
        # if not robbing then solve nums[i+1]
        # if robbing then solve nums[i] + nums[i+2]
        # take the max solution
        # using memoization
        memo = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(dfs(i+1), nums[i] + dfs(i+2))
            return memo[i]

        return dfs(0)