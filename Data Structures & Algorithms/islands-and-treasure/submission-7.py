class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # BFS for nearest distance
        # Multi source BFS

        # Time complexity: O(MN) space: O(1)

        ROWS, COLS = len(grid), len(grid[0])

        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        queue = deque()
        visited = set()

        # staring cells for the BFS
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))

        count = 0

        while queue:

            for _ in range(len(queue)):
                r, c = queue.popleft()

                grid[r][c] = count
                for r_off, c_off in directions:
                    nr, nc = r + r_off, c + c_off
                    
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == -1 or (nr, nc) in visited:
                        continue
                    
                    queue.append((nr,nc))
                    visited.add((nr,nc))

            count += 1