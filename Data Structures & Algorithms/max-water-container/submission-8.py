class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1
        maxArea = 0
        
        # 0, 7
        while (l < r):
            maxHeight = min(heights[l], heights[r])
            print(heights[l], heights[r])
            maxArea = max(maxArea, maxHeight * (r-l))
            print(maxArea)
            if(heights[l] < heights[r]):
                l += 1
            else:
                r -= 1
        return maxArea

        