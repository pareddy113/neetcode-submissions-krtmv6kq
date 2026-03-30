class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_map = defaultdict(int)
        l, r = 0, 0
        max_count = 0

        while r < len(s):
            # Increment the count of the character at the right pointer
            s_map[s[r]] += 1

            while (r - l + 1) - max(s_map.values()) > k:
                # Decrement the count of the character at the left pointer
                s_map[s[l]] -= 1
                # Move the left pointer to shrink the window
                l += 1

            # Update the maximum length of the valid substring
            max_count = max(max_count, r - l + 1)
            # Move the right pointer to expand the window
            r += 1

        # Return the maximum length of the substring found
        return max_count
