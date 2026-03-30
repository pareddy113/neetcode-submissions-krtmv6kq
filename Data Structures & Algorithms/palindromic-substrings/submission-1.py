class Solution:
    def countSubstrings(self, s: str) -> int:
               # odd length
        count = 0
        i = 0
        while (i < len(s)):
            l,r = i, i
            while(l >= 0 and r < len(s)):
                if s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1

                else:
                    break
        
            l,r = i, i+1
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                count += 1
                l -= 1
                r += 1
            i += 1
        
        return count
                
