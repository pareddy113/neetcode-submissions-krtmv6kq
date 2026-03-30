class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[False for _ in range(m)] for _ in range(n)]
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0

            if i == 0 and j == 0:
                return 1 

            return dfs(i - 1, j) + dfs(i, j - 1)
        
        return dfs(m - 1, n - 1)