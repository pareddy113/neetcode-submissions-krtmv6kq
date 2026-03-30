from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()  # important for skipping duplicates

        def backtrack(start: int):
            res.append(subset[:])
            for i in range(start, len(nums)):
                # Skip duplicates: only pick the *first* duplicate in the same recursion layer
                if i == start or nums[i] != nums[i - 1]:     
                    subset.append(nums[i])
                    backtrack(i + 1)
                    subset.pop()

        backtrack(0)
        return res