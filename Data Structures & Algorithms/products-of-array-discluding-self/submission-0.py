class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # [1,2,4,6]
        # [1, 1, 2, 8]
        # [48,24,6,1]
        #[48, 24, 12, 8]

        res = [1] * len(nums)
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        # [1,1,2,8]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        # [1,1,1,1] index = 2, 1, 0
        for j in range(len(nums) - 2, -1, -1):
            print(j)
            suffix[j] = suffix[j+1] * nums[j+1]
        
        print(prefix)
        print(suffix)
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
        return res
        