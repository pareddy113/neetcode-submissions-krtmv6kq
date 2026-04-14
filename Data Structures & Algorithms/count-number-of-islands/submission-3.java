class Solution {
    private int rowSize;
    private int colSize;
    private int[][] directions = {{1,0}, {-1,0}, {0,1}, {0,-1}};

    public int numIslands(char[][] grid) {
        rowSize = grid.length;
        colSize = grid[0].length;
        int numOfIslands = 0;

        System.out.println(rowSize);
        System.out.println(colSize);
        for(int r = 0; r < rowSize; r++) {
            for(int c = 0; c < colSize; c++) {
                if (grid[r][c] == '1') {
                    dfs(r, c, grid);
                    numOfIslands++;
                }
            }
        }
        return numOfIslands;
    }

    private void dfs(int r, int c, char[][] grid) {
        
        if (r < 0 || r >= rowSize || c < 0 || c >= colSize || grid[r][c] != '1') return;

        grid[r][c] = '0';

        for(int[] direction: directions) {
            dfs(r + direction[0], c + direction[1], grid);
        }
    }
}
