class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i):
            # Base Case: If we reached the end, we found 1 valid way
            if i == len(s):
                return 1
            
            # Base Case: Leading zero cannot be decoded
            if s[i] == '0':
                return 0
            
            if i in memo:
                return memo[i]

            # Choice 1: Take 1 digit (Always valid if not '0')
            res = dfs(i + 1)

            # Choice 2: Take 2 digits (Valid if 10-26)
            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] in "0123456")):
                res += dfs(i + 2)

            memo[i] = res
            return res

        return dfs(0)