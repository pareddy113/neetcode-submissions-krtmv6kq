class Solution:
    def numDecodings(self, s: str) -> int:

        num_set = { str(i) for i in range(1, 27) }
        
        def decodeDfs(i):
            
            if i == len(s):
                return 1

            if s[i] not in num_set:
                return 0
            
            res = 0
            # CHOICE 1: Try taking a 1-digit slice s[i : i+1]
            if i + 1 <= len(s) and s[i : i+1] in num_set:
                res += decodeDfs(i + 1)
                
            # CHOICE 2: Try taking a 2-digit slice s[i : i+2]
            if i + 2 <= len(s) and s[i : i+2] in num_set:
                res += decodeDfs(i + 2)
            
            return res

        
        return decodeDfs(0)
        