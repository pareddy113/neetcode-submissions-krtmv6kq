class Solution:
    def rob(self, nums: List[int]) -> int:


        def helper(nums):
            rob1, rob2 = 0, 0

            for num in nums:
                newRob = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = newRob
            return rob2

        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))


        # if len(nums) == 1:
        #     return nums[0]

        # memo = [[-1] * 2 for _ in range(len(nums))]

        # def dfs(i, flag):
        #     if i >= len(nums) or (flag and i == len(nums) - 1):
        #         return 0
        #     if memo[i][flag] != -1:
        #         return memo[i][flag]
        #     memo[i][flag] = max(dfs(i + 1, flag),
        #                     nums[i] + dfs(i + 2, flag or (i == 0)))
        #     return memo[i][flag]

        # return max(dfs(0, True), dfs(1, False))