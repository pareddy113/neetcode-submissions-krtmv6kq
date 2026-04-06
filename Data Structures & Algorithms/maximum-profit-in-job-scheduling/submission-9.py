import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        items=[(i,j,k) for i,j,k in zip(startTime, endTime, profit)]
        items.sort()
        
        # [(2, 5, 2), (2, 8, 4), (4, 5, 1), (4, 5, 8), (8, 10, 10)]
        # 
        cache = {}

        def max_profit(i):

            if i == len(profit):
                return 0
            
            if i in cache:
                return cache[i]

            res = max_profit(i + 1)

            # 0,1,2,3,4,5,6,7
            # 1,2,

            # figure out which index should be picked next with no overlapping
            index = bisect.bisect_right(items, (items[i][1], 0, 0))
            cache[i] = res = max(res, items[i][2] + max_profit(index))
            return res
        
        return max_profit(0)
            



        