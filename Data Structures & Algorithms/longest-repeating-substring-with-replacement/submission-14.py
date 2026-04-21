class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_map = defaultdict(int)
        l, r = 0, 0
        max_count = 0
        max_value = 0

        while r < len(s):
            # Increment the count of the character at the right pointer
            s_map[s[r]] += 1

            # maintain the max value so far
            max_value = max(max_value, s_map[s[r]])
            r += 1

            while (r - l) - max_value > k:        
                s_map[s[l]] -= 1
                l += 1

            max_count = max(max_count, r - l)            

        # Return the maximum length of the substring found
        return max_count
