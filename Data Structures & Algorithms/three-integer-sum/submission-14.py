class Solution:
            
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-1,0,1,2,-1,-4]
        # [-3, -1, 1, 0, 1, 2, 4]
        # [-3, -1, 4], [-3, 1, 2 ]
        nums.sort()
        res = []
        for i in range(len(nums)):
            target = nums[i]
            l = i + 1
            r = len(nums) - 1

            if ( i > 0 and nums[i] == nums[i - 1]):
                continue

            while(l < r):
                if nums[l] + nums[r] + target > 0:
                    r -= 1
                elif nums[l] + nums[r] + target < 0:
                    l += 1
                else:
                    res.append([nums[l], nums[r], target])
                    l += 1
                    r -= 1

                    while(l < r and nums[l] == nums[l-1]):
                        l += 1 
                    while(l < r and nums[r] == nums[r+1]):
                        r -= 1 
        return res






