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
            localCapacityWithDist = 0
            if (heights[l] < heights[r]):
                minHeight = min(heights[l], heights[r])
                localCapacity = minHeight * (r-l)
                l += 1
            elif (heights[l] > heights[r]):
                minHeight = min(heights[l], heights[r])
                localCapacity = minHeight * (r-l)
                r -= 1
            else:
                localCapacity = heights[l] * (r-l)
                l +=  1
                r -= 1
            maxCapacity = max(maxCapacity, localCapacity)
        return maxCapacity


        