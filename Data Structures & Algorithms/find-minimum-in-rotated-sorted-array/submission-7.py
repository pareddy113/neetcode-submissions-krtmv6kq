class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [1,2,3, 4 ,5,6,7]
        # [7,1,2, 3 ,4,5,6]
        # [6,7,1, 2 ,3,4,5]
        # [5,6,7, 1 ,2,3,4]
        # [4,5,6, 7 ,1,2,3]
        
        # [6,5, 4, 3,2,1]
        # [5,6,1,2,3,4]
         # [4,5,6,1,2,3,4]

        # it 1: l = 0, r=5,m = 2, l = 3
        # it 2: l = 3, r = 5, m = 4 -> r = 4
        # it 3: l = 3, r = 4, m = 3 -> l = 4
        right = len(nums) - 1
        left = 0
        minValue = float("inf")

        while(left <= right):
            mid = left + (right-left)//2
            minValue = min(minValue, nums[mid])
            if (nums[mid] < nums[right]):
                right = mid - 1
            else:
                left = mid + 1
        return minValue

        
        