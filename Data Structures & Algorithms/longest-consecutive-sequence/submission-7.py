class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        output = 0
        i = 0
        for val in numSet:
            if val - 1 not in numSet:
                localCount = 1
                while(val + localCount in numSet):
                    localCount += 1
                output = max(localCount, output)
            i += 1
        return output
