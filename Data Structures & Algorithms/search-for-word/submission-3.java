class Solution {

    boolean ans = false;

    public boolean exist(char[][] board, String word) {
        
        for(int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                dfs(board, i, j, word, 0);
            }
        }
        return ans;
    }

    public void dfs(char[][] board, int r, int c, String word, int index) {

        if (word.length() == index) {
            ans = true;
            return;
         }

        if (r < 0 || r >= board.length || c < 0 || c >= board[0].length ||
         board[r][c] != word.charAt(index) || board[r][c] == '#') {
            return;
         }

        board[r][c] = '#';

         dfs(board, r + 1, c, word, index + 1);
         dfs(board, r - 1, c, word, index + 1);
         dfs(board, r, c + 1, word, index + 1);
         dfs(board, r, c - 1, word, index + 1);

         board[r][c] = word.charAt(index);
    }
}
