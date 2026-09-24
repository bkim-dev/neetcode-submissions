class Solution:
    def rob(self, nums: List[int]) -> int:
        # starting at i = 1
        # check to rob or not rob a house
        # if not robbing then solve nums[i+1]
        # if robbing then solve nums[i] + nums[i+2]
        # take the max solution
        # using tabularization
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return dp[-1]