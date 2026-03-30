class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        # 0, 7 - 3 = 4
        # {3: 0, }
        for i in range(len(nums)): 
            rem = target - nums[i]
            if rem in map:
                return [map[rem], i]
            map[nums[i]] = i
