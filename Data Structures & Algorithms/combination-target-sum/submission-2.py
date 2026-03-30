class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []

        def combSum(start, target):
            if target == 0:
                res.append(comb[:])
            
            if target < 0:
                return

            for i in range(start, len(nums)):
                comb.append(nums[i])
                combSum(i, target - nums[i])
                comb.pop()
        combSum(0, target)
        return res
        