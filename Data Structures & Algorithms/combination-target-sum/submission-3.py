class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # [2,5,6,9] -> 9
        #               []
        #  2             5           6       9
        # 2 5 6 9     5 6 9 
        res = []
        def sum(start, currTarget, currList):

            print(start, currTarget, currList)
            if (currTarget < 0):
                return

            if (currTarget == 0):
                res.append(currList.copy())
                return

            for i in range(start, len(nums)):
                currList.append(nums[i])
                sum(i, currTarget - nums[i], currList)
                currList.pop()
        
        sum(0, target, [])
        return res

        