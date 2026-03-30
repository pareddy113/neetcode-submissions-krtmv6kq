class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def capture(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS):
                return
            
            if (r,c) in visited or board[r][c] != "O":
                return

            visited.add((r,c))
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        for r in range(ROWS):
            capture(r, 0)
            capture(r, COLS - 1)

        for c in range(COLS):
            capture(0, c)
            capture(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and board[r][c] == "O":
                    board[r][c] = "X"