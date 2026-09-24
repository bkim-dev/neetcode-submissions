class Solution:
    def climbStairs(self, n: int) -> int:
        # can step either n+1 or n+2 distance
        one = 1
        two = 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one