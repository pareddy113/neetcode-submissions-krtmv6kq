class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs
        # sort each string & sorting all & group the

        sortedStrs = [''.join(sorted(strs[i])) for i in range(len(strs))]
        # unsorted ordered map
        # [ba, cb, ab, bc , c]
        # sorted ordered map
        # [ab, bc, ab, bc , c]

        # group them and
        ans = {}
        for i, sortedStr in enumerate(sortedStrs):
            if sortedStr not in ans:
                ans[sortedStr] = [strs[i]]
            else:
                ans[sortedStr].append(strs[i])
        return ans.values()
        