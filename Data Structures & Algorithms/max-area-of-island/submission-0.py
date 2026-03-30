class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rowLen, colLen = len(grid), len(grid[0])

        def maxAreaDfs(r, c):
        
            if r <0 or c < 0 or r >= rowLen or c >= colLen or grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            return 1 + maxAreaDfs(r-1, c) + maxAreaDfs(r + 1, c) + maxAreaDfs(r, c + 1)+ maxAreaDfs(r, c - 1)


        area = 0

        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == 1:
                    area = max(area, maxAreaDfs(i, j))

        return area