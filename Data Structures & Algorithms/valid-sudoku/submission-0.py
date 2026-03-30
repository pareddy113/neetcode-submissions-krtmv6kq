class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row[i] = [()]
        # col[j] = [()]
        # block[i//3, j//3] = [()]
        # not in row or not in col or not in block
        rowLength = len(board)
        colLength = len(board[0])
        rows = [set() for _ in range(rowLength)]
        cols = [set() for _ in range(colLength)]
        numOfBlocks = (rowLength//3) * (colLength//3)
        block = [set() for _ in range(numOfBlocks)]
        
        for i in range(rowLength):
            for j in range(colLength):
                blockI, blockJ = i//3, j//3
                blockNum = (blockI * 3) + blockJ
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i]:
                    print(rows)
                    return False
                if board[i][j] in cols[j]:
                    print(cols)
                    return False
                if board[i][j] in block[blockNum]:
                    print(block)
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                block[blockNum].add(board[i][j])
        return True
                    
