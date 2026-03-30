class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        rep = 0
        while(i < len(nums) - 1):
            if (i <= rep):
                return False
            i = i + nums[i]
            rep = max(rep, i)
            if (i >= len(nums) - 1):
                return True
        return False


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        for i in range(len(nums)):
            if i > max_reachable:
                return False  # If the current index is not reachable, we fail
            max_reachable = max(max_reachable, i + nums[i])
            if max_reachable >= len(nums) - 1:
                return True  # If we can reach or exceed the last index, succeed
        return False
