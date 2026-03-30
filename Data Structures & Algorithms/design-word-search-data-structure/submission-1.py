class TreeNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = TreeNode()
            curr = curr.children[i]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        
        def searchDfs(i, curr):
            if (i == len(word)):
                return curr.end

            if word[i] == ".":
                for ch in curr.children.values():
                    if searchDfs(i + 1, ch):
                        return True
                return False
            else:
                if word[i] not in curr.children:
                    return False
                return searchDfs(i + 1, curr.children[word[i]])
        
        return searchDfs(0, self.root)
