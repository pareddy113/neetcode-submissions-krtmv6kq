class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        def par(l, r, currList):
            
            if l == r == n:
                res.append("".join(currList))
                return
            
            if (l < n):
                currList.append("(")
                par(l + 1, r, currList)
                currList.pop()
            
            if (r < l):
                currList.append(")")
                par(l, r + 1, currList)
                currList.pop()

        par(0, 0, [])
        return res
