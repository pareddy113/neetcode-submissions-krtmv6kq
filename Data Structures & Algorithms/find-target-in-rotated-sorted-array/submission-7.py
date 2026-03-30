class Solution:

    # [3,4, 5 ,6,1,2]  target=1
    # l = 3, r = 5, m = 4

    # [1,3] l=0, r=1, m=0 1<3 1
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while(l <= r):
            mid = l + (r-l)//2
            if (nums[mid] == target):
                return mid
            
            if (nums[mid] <= nums[r]):
                if(nums[mid] <= target) and (nums[r] >= target):
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if(nums[l] <= target) and (nums[mid] >= target):
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


