class Solution {
    /*
        9x9 board
        row unique,
        col unique,
        sub-box unique

        HashMap<Integer, HashSet<Character>>

        0 - 9
        0,1,2
        0,1,2

        0,1,2
        3,4,5
    */
    public boolean isValidSudoku(char[][] board) {
        
        Map<Integer, Set<Character>> rowSet = new HashMap<>();
        Map<Integer, Set<Character>> colSet = new HashMap<>();
        Map<Integer, Set<Character>> blockSet = new HashMap<>();
        
        for(int r = 0; r < board.length; r++) {
            for(int c = 0; c < board[0].length; c++) {
                
                if (board[r][c] == '.') {
                    continue;
                }
                // figure row
                int blockNum = ((r / 3) * 3) + (c / 3);
                rowSet.putIfAbsent(r, new HashSet<Character>());
                colSet.putIfAbsent(c, new HashSet<Character>());
                blockSet.putIfAbsent(blockNum, new HashSet<Character>());

                if(rowSet.get(r).contains(board[r][c]) || colSet.get(c).contains(board[r][c]) || blockSet.get(blockNum).contains(board[r][c])){
                    return false;
                }
                rowSet.get(r).add(board[r][c]);
                colSet.get(c).add(board[r][c]);
                blockSet.get(blockNum).add(board[r][c]);
        }
    }
    return true;
  }
}
