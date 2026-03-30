class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        charMap = {}
        counter = 0
        longest = 0
        while (r < len(s)):
            if (charMap.get(s[r], 0) > 0):
                counter += 1
            charMap[s[r]] = charMap.get(s[r], 0) + 1
            r += 1

            while (counter > 0):
                print(charMap)
                charMap[s[l]] = charMap.get(s[l], 0) - 1
                if (charMap[s[l]] > 0):
                    counter -= 1
                l += 1
            longest = max(longest, r - l)

        return longest
            
            
                

        