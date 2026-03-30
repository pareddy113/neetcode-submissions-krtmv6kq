class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = defaultdict(int)
        

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            map[s[i]] += 1
            map[t[i]] -= 1
        return True if max(map.values()) ==0 else False