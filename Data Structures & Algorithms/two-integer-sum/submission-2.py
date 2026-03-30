class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in countMap:
                return [countMap[diff], i]
            countMap[nums[i]] = i

        
        

        