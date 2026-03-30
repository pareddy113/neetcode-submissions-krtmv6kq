class Solution:
    def twoSum(self, nums, i, output):
        target = nums[i]
        left, right = i + 1, len(nums) - 1

        while(left < right):
            twoSum = nums[left] + nums[right]

            if (twoSum + target < 0):
                left += 1
            elif (twoSum + target > 0):
                right -= 1
            else:
                output.append([target, nums[left] ,nums[right]])
                left += 1
                right -=1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -=1
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                self.twoSum(nums, i, res)
        return res