class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #tabularization / bottom-up
        n = len(cost)
        dp = [0] * (n+1) # initialize a table of size n+1 (includes end of staircase)
        
        for i in range(2, n+1): #check i-1 and i-2 costs from 2 to n+1
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[n]
        