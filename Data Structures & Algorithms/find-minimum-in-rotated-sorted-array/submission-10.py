class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [1,2, 3, 4,5,6] > l <l
        # [6,1, 2, 3,4,5] < l <l
        # [5,6, 1, 2,3,4] < m <m
        # [4,5, 6, 1,2,3] > r >r
        # [3,4, 5, 6,1,2] > r >r
        # [2,3, 4, 5,6,1] > r >r
        curr_min = float('inf')
        l, r = 0, len(nums) - 1
        while (l <= r):
            mid = (l + r)//2
            curr_min = min(curr_min, nums[mid])
            # left sorted
            if (nums[mid] > nums[r]):
                l = mid + 1
            # right sorted
            else:
                r = mid - 1
        return curr_min
    