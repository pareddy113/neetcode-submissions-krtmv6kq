class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def robDfs(i):
            if i >= n:
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(nums[i] + robDfs(i + 2), robDfs(i + 1))
            return memo[i]

        return max(robDfs(0), robDfs(1))