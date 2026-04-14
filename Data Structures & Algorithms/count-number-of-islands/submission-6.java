class Solution {
    private int rowSize;
    private int colSize;
    private int[][] directions;
    boolean[][] visited;
    ArrayDeque<int[]> queue;

    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        
        this.queue = new ArrayDeque<>();
        this.rowSize = grid.length;
        this.colSize = grid[0].length;
        this.directions = new int[][]{{1,0}, {-1,0}, {0,1}, {0,-1}};
        
        int numOfIslands = 0;

        for(int r = 0; r < rowSize; r++) {
            for(int c = 0; c < colSize; c++) {
                if (grid[r][c] == '1') {
                    queue.addLast(new int[]{r,c});
                    bfs(grid);
                    numOfIslands++;
                }
            }
        }
        return numOfIslands;
    }

    private void bfs(char[][] grid) {

       while(queue.size() > 0) {
            int[] cell = queue.pollFirst();
            grid[cell[0]][cell[1]] = '0';
            for(int[] direction: directions) {
                int r = cell[0] + direction[0];
                int c = cell[1] + direction[1];
                if (r < 0 || r >= rowSize || c < 0 || c >= colSize || grid[r][c] != '1') continue;
                queue.addLast(new int[]{r,c});
            }
       }
       
    }
}
