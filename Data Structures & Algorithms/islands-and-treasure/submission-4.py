class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # find the neareast treasure for each valid(INF) cell
        ROWS, COLS = len(grid), len(grid[0])

        queue = deque()
        visited = set()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))
        # print(queue)
        # print(visited)
        # [(0,2), (3,0)]
        # x,y=0,2
        count = 1
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for i,j in [(1,0),(0,1),(-1,0),(0, -1)]:
                    dx, dy = x+i, y+j

                    if dx < 0 or dy < 0 or dx >= ROWS or dy >= COLS or grid[dx][dy] == -1 or (dx, dy) in visited:
                        continue

                    grid[dx][dy] = count
                    queue.append((dx, dy))
                    visited.add((dx, dy))
            count+=1



