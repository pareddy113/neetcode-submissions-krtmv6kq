class Solution:
    def climbStairs(self, n: int) -> int:

        memo = defaultdict(int)
        def dfs(i):

            if i == 0:
                return 1
            if i == 1:
                return 1
            if memo[i]:
                return memo[i]

            memo[i] = dfs(i - 1) + dfs(i - 2)
            return memo[i]
     
        # 1, 0
        return dfs(n)