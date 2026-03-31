class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 34 def ghi
        # "" d e f
        key_map = {2: "abc", 3: "def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        n = len(digits)
        res = []

        def dfs(comb, index):
            if len(digits) == 0:
                return
                
            if len(comb) == n:
                res.append("".join(comb[:]))
                return
            
            for i in key_map[int(digits[index])]:
                comb.append(i)
                dfs(comb, index + 1)
                comb.pop()

        dfs([], 0)
        return res

