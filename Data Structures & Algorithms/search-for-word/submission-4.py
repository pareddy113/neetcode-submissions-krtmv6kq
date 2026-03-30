class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        colLen = len(board[0])
        rowLen = len(board)
        visited = [[False for _ in range(colLen)] for _ in range(rowLen)]
        
        def dfs(i, j, index):
            
            if (i < 0 or j < 0 or i >= rowLen or j >= colLen or board[i][j] != word[index]):
                return False

            if visited[i][j]:
                return False

            if index == len(word) -1:
                return True

            visited[i][j] = True

            found = (dfs(i + 1, j, index + 1) or 
            dfs(i - 1, j, index + 1) or
            dfs(i, j + 1, index + 1) or
            dfs(i, j - 1, index + 1))

            visited[i][j] = False
            return found


        
        for i in range(rowLen):
            for j in range(colLen):
                if dfs(i, j, 0):
                    return True
        return False
