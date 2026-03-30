class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # Multi source BFS

        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
        queue = deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append([r, c])
                    visited[r][c] = True
        
        time = 0
        while queue and fresh > 0:

            for _ in range(len(queue)):
                r,c = queue.popleft()

                for dr,dc in [(1,0), (0,1),(-1,0),(0,-1)]:
                    nr, nc = r + dr, c + dc

                    if 0<= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append([nr, nc])
                        fresh -= 1

            time += 1
        return time if fresh == 0 else -1