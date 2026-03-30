class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # 0 -> empty ,1 -> fresh ,2 -> rotten
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        
        freshCount = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshCount += 1

                if grid[r][c] ==  2:
                    queue.append((r,c))
                    visited.add((r,c))
        
        minTime = 0
        while queue and freshCount > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for nr, nc in [(1,0),(0,1),(-1,0),(0,-1)]:
                    tr, tc = r + nr, c + nc

                    if tr < 0 or tc < 0 or tr >= ROWS or tc >= COLS or grid[tr][tc] != 1 or (tr,tc) in visited:
                        continue
                    
                    freshCount -= 1
                    queue.append((tr, tc))
                    visited.add((tr,tc))
            minTime += 1
        
        return -1 if freshCount > 0 else minTime
                    


        