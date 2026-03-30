class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while (l <= r):
            if (nums[l] <= nums[r]):
                return nums[l]
            
            mid = (l + r) // 2
            print("mid=", nums[mid])

            if (nums[mid] >= nums[l]):
                l = mid + 1
            else:
                r = mid
            print([nums[l], nums[r]])
        return -1



        