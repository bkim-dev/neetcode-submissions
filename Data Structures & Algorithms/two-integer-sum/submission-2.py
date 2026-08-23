class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])

        A.sort()
        l = 0
        r = len(nums) - 1
        while l < r:
            cur = A[l][0] + A[r][0]
            if cur == target:
                return [min(A[l][1], A[r][1]), max(A[l][1], A[r][1])]
            elif cur < target:
                l += 1
            else:
                r -= 1
        return []
