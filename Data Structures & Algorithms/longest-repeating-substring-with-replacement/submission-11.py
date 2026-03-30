class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        longest = 0
        charMap = defaultdict(int)

        while (r < len(s)):
            ch = s[r]
            charMap[ch] = charMap[ch] + 1
            r += 1
            while ((r - l) - max(charMap.values()) > k):
                charMap[s[l]] = charMap[s[l]] - 1
                l += 1
            
            longest = max(longest, r - l)

        return longest
