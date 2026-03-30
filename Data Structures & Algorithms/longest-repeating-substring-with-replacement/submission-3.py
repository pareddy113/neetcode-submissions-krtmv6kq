class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_map = defaultdict(int)
        l, r = 0, 0
        max_count = 0

        while (r < len(s)):
            s_map[s[r]] += 1
            while ((r - l + 1) - max(s_map.values())) > k:
                s_map[s[l]] -= 1
                l += 1
            max_count = max(max_count, r - l + 1)
            r += 1
        return max_count 