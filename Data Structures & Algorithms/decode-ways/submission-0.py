class Solution:
    def numDecodings(self, s: str) -> int:
        count = 0
        def rec(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            
            count = rec(i + 1)
            if i + 1 < len(s) and int(s[i: i+2]) <= 26:
                count = count + rec(i + 2)
        
            return count

        return rec(0)