class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        
        def minDfs(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]

            
            memo[i] = cost[i] + min(minDfs(i + 1), minDfs(i + 2))
            return memo[i]
        
        return min(minDfs(0), minDfs(1))