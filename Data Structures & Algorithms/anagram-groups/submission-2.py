class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs
        # sort each string & sorting all & group the
        # unsorted ordered map
        # [ba, cb, ab, bc , c]
        # sorted ordered map
        # [ab, bc, ab, bc , c]

        # group them and
        ans = defaultdict(list)
        for string in strs:
            count = [0 for _ in range(26)]
            for j in string:
                count[ord(j) - ord('a')] += 1
            ans[tuple(count)].append(string)
        return ans.values()
        