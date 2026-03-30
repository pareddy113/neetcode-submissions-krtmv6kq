class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n = 2
        # []
        # (         [)]
        # ((            ()
        # [(((] (()     ()(     [())]
        res = []
        bra = ["(", ")"]

        def par(l, r, currList):
            if r > l or l > n:
                return

            if l == n and r == n:
                tempList = currList[:]
                res.append("".join(tempList))
                return
            
            for i in bra:
                currList.append(i)
                if (i == "("):
                    l += 1
                else:
                    r += 1
                par(l, r, currList)
                if (i == "("):
                    l -= 1
                else:
                    r -= 1
                currList.pop()

        par(0, 0, [])
        return res
