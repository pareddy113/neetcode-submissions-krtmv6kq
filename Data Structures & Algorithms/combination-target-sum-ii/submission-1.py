class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        candidates.sort()
        def combSum(start, target):
            if target == 0:
                res.append(comb[:])
            
            if target < 0:
                return

            for i in range(start, len(candidates)):
                if (start == i or candidates[i] !=  candidates[i - 1]):
                    comb.append(candidates[i])
                    combSum(i + 1, target - candidates[i])
                    comb.pop()
        combSum(0, target)
        return res
        