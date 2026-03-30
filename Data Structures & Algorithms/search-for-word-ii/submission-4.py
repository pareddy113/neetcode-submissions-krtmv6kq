class TrieNode:

    def __init__(self) -> None:
        self.children= {}
        self.word = None

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # a
        # s,        b
        # a, a      c, a
        # create a Trie
        root = TrieNode()
        for word in words:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.word = word

        res = []
        rowLength = len(board)
        colLength = len(board[0])
        
        def dfs(r, c, node):
            if r < 0 or c < 0 or r>= rowLength or c >= colLength:
                return
            ch = board[r][c]
            
            if ch == "#" or ch not in node.children:
                return
            
            curr_node = node.children[ch]
            if curr_node.word is not None:
                res.append(curr_node.word)
                curr_node.word = None

            board[r][c] = "#"
            
            dfs(r - 1, c, curr_node)
            dfs(r + 1, c, curr_node)
            dfs(r, c - 1, curr_node)
            dfs(r, c + 1, curr_node)

            board[r][c] = ch
        
        for i in range(rowLength):
            for j in range(colLength):
                dfs(i , j, root)
        
        return res
