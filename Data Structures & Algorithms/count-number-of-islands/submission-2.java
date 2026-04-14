class Solution {
    private int rowSize;
    private int colSize;

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
        dfs(r + 1, c, grid);
        dfs(r - 1, c, grid);
        dfs(r, c + 1, grid);
        dfs(r, c - 1, grid);
    }
}
