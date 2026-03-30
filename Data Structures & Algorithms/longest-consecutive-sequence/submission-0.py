class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longestSeq = 0
        uniqueNums = set(nums)
        i = 0
        while (i < len(nums)):
            if (nums[i]-1) not in uniqueNums:
                count = 1
                while (nums[i] + count in uniqueNums):
                    count += 1
                longestSeq = max(longestSeq, count)
                count = 0
            i += 1
        return longestSeq
                
        