class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS, COLS = len(grid), len(grid[0])

        queue = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))
        
        count = 0
        while queue:
            for cell in range(len(queue)):
                r, c = queue.popleft()

                grid[r][c] = count
                for r_off, c_off in [(0,1), (1,0), (0, -1), (-1, 0)]:
                    nr, nc = r + r_off, c + c_off
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != -1 and (nr, nc) not in visited:
                        queue.append((nr,nc))
                        visited.add((nr,nc))
            count += 1