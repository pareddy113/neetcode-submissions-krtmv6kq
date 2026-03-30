from typing import List

class Solution:
    def twoSum(self, nums: List[int], start: int, target: int, ans: List[List[int]]):
        left, right = start + 1, len(nums) - 1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum + target < 0:
                left += 1
            elif current_sum + target > 0:
                right -= 1
            else:
                ans.append([target, nums[left], nums[right]])
                left += 1
                right -= 1
                # Skip duplicates for `left`
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                # Skip duplicates for `right`
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
        return ans

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()  # Sort the array first
        for i in range(len(nums)):
            # Skip duplicates and stop if the number is greater than 0
            if i == 0 or nums[i] != nums[i - 1]:
                self.twoSum(nums, i, nums[i], output)
        return output

# Example usage
solution = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(solution.threeSum(nums))
