class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = float("-inf")
        curr_max = 1
        curr_min = 1
        

        for num in nums:
            tmp = curr_min * num
            curr_min = min(curr_max * num, curr_min * num, num)
            curr_max = max(curr_max * num, tmp, num)
            max_product = max(max_product, curr_max)
        return max_product
        