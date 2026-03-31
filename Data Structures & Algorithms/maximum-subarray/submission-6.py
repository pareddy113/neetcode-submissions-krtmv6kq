class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        l = r = 0
        max_sum = float("-inf")
        n = len(nums)
        start = 0
        prev_sum = 0

        for i in nums:
            prev_sum = max(prev_sum + i, i)
            max_sum = max(max_sum, prev_sum)
        return max_sum