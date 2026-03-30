class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        colLen = len(board[0])
        rowLen = len(board)
        
        def dfs(i, j, index):
            
            if (i < 0 or j < 0 or i >= rowLen or j >= colLen or board[i][j] != word[index]):
                return False

            if index == len(word) -1:
                return True

            temp = board[i][j]
            board[i][j] = "#"

            found = (dfs(i + 1, j, index + 1) or 
            dfs(i - 1, j, index + 1) or
            dfs(i, j + 1, index + 1) or
            dfs(i, j - 1, index + 1))

            board[i][j] = temp
            return found


        
        for i in range(rowLen):
            for j in range(colLen):
                if dfs(i, j, 0):
                    return True
        return False
