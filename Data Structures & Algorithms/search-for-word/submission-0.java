public class Solution {
    private int ROWS, COLS;
    boolean ans = false;
    
    public boolean exist(char[][] board, String word) {
        ROWS = board.length;
        COLS = board[0].length;
        

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                dfs(board, word, r, c, 0);
            }
        }
        return ans;
    }

    private void dfs(char[][] board, String word, int r, int c, int i) {
        if (i == word.length()) {
            ans = true;
            return;
        }
        if (r < 0 || c < 0 || r >= ROWS || c >= COLS || 
            board[r][c] != word.charAt(i) || board[r][c] == '#') {
            return;
        }

        board[r][c] = '#';
        dfs(board, word, r + 1, c, i + 1);
        dfs(board, word, r - 1, c, i + 1);
        dfs(board, word, r, c + 1, i + 1);
        dfs(board, word, r, c - 1, i + 1);
        System.out.println(r + " , " + c);
        board[r][c] = word.charAt(i);
    }
}