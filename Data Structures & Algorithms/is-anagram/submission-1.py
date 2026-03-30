class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charListS = [0 for _ in range(26)]
        charListT = [0] * 26

        if (len(s) != len(t)):
            return False

        for i in range(len(s)):
            charListS[ord(s[i]) - ord('a')] += 1
            charListT[ord(t[i]) - ord('a')] += 1
        
        return charListS == charListT