class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rowLen, colLen = len(grid), len(grid[0])

        def dfs(r,c):

            if r < 0 or c < 0 or r >= rowLen or c >= colLen or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        maxArea = 0
        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea