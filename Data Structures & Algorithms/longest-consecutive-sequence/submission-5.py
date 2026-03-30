class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        output = 0
        i = 0
        while(i < len(nums)):
            localCount = 1
            val = nums[i]
            while(val + 1 in numSet):
                localCount += 1
                val += 1
                print(nums[i], localCount)
            output = max(localCount, output)
            i += 1
        return output
