class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = [0] * 26
        

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            map[ord(s[i]) - ord('a')] += 1
            map[ord(t[i]) - ord('a') ] -= 1
        return True if max(map)==0 else False