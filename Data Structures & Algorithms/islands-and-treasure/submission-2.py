class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append([i, j])
                    visited[i][j] = True
        
        distance = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                grid[r][c] = distance

                for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] != -1 and not visited[nr][nc]:
                        queue.append([nr, nc])
                        visited[nr][nc] = True
            distance += 1


        
