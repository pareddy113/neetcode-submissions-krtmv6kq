class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        localSum = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            localSum = max(localSum + nums[i], nums[i])
            maxSum = max(maxSum, localSum)
        return maxSum

        