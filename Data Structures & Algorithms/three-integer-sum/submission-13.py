class Solution:
            
    def twoSum(self, partialNums, target):
        l = 0
        r = len(partialNums) - 1
        resp = []
        while ( l < r):
            if partialNums[l] + partialNums[r] > -target:
                print(">", partialNums[l], partialNums[r], target)
                r -=1
            elif partialNums[l] + partialNums[r] < -target:
                print("<", partialNums[l], partialNums[r], target)
                l += 1
            else:
                print("=", partialNums[l], partialNums[r], target)
                resp.append([partialNums[l], partialNums[r], target])
                r -= 1
                l += 1
        return resp

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            print(nums[:i] + nums[i+1:], nums[i])
            resp = self.twoSum(nums[:i] + nums[i+1:], nums[i])
            print(resp)
            
            if len(resp)>0:
                sortList = [sorted(i) for i in resp]
                [res.add(tuple(i)) for i in sortList]
        return [list(i) for i in res]


