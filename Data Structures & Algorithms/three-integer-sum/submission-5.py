class Solution:
    def twoSum(self, nums:List[int], start: int, target: int, ans:List[List[int]]):
        # Sorted nums
        # num1 + num2 = target
        # target = 2
        # [-4,-1,-1,0,1,2]
        left, right = start + 1, len(nums) - 1
        while (left < right):
            if (nums[left] + nums[right] < -target):
                left += 1
            elif (nums[left] + nums[right] > -target):
                right -= 1
            else:
                ans.append([target, nums[left], nums[right]])
                left += 1
                right -= 1
                while (nums[left] == nums[left - 1] and left < right):
                    left += 1
        return ans


    def threeSum(self, nums: List[int]) -> List[List[int]]:

        output = []
        # Input: nums = [-1,0,1,2,-1,-4]
        sortNums = sorted(nums)
        # Input: sortedNums = [-4,-1,-1,0,1,2]
        for i in range(len(nums)):
            if (i == 0 or sortNums[i] != sortNums[i-1]):
                first = sortNums[i]
                self.twoSum(sortNums, i, first, output)
        return output







        