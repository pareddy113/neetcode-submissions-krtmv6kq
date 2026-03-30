class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # [1,7,2,5,4,7,3,6]
        # l = 0
        # r = 6
        l = 0
        r = len(heights) - 1
        maxCapacity = 0
        while (l < r):
            localCapacity = 0
            localCapacity = min(heights[l], heights[r]) * (r-l)
            if (heights[l] < heights[r]):
                l += 1
            elif (heights[l] >= heights[r]):
                r -= 1
            maxCapacity = max(maxCapacity, localCapacity)
        return maxCapacity


        