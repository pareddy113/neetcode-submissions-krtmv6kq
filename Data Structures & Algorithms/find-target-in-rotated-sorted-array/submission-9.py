class Solution:
    # find the sorted half of the array
    # figure out if the target is in this sorted array, if not search the other half
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while (start <= end):
            mid = (start + end) // 2

            if (nums[mid] == target):
                return mid

            # left sorted
            if (nums[mid] >= nums[start]):
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            # right sorted
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
                    
        