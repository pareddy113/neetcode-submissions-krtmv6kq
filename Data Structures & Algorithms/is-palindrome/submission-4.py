class Solution:
    def isPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1

        while(l <= r):
            if not self.isAlphaNumeric(s[l]):
                l+=1
                continue
            if not self.isAlphaNumeric(s[r]):
                r-=1
                continue
            
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True
        


    def isAlphaNumeric(self, c):
        cNum = ord(c.lower())
        return ord('a') <= cNum <= ord('z') or ord('0') <= cNum <= ord('9')