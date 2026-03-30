class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        longest = 0
        counter = 0 # keep track of distinct alph
        charMap = defaultdict(int)

        while (r < len(s)):
            ch = s[r]
            if (charMap[ch] == 0):
                counter += 1
            charMap[ch] = charMap[ch] + 1
            r += 1
            print(charMap, counter)
            while ((r - l) - max(charMap.values()) > k):
                print("loop", charMap, counter, longest)
                charMap[s[l]] = charMap[s[l]] - 1

                if (charMap[s[l]] == 0):
                    counter -= 1
                l += 1
            
            longest = max(longest, r - l)
        return longest
