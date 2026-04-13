import heapq

from functools import lru_cache

class Solution:
    def maximumProfit2(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(weight)

        @lru_cache
        def dfs(i, c):
            if i == n:
                return 0
            if c == 0:
                return 0
            
            if weight[i] <= c:
                return max(profit[i] + dfs(i, c - weight[i]), dfs(i + 1, c))
            else:
                return dfs(i + 1, c)

        return dfs(0, capacity)


    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(weight)

        dp = [[0] * (capacity + 1) for _ in range(n + 1)]

        for c in range(capacity + 1):
            dp[n][c] = 0
        
        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(n-1, -1, -1): # n - 1 to 0
            for c in range(1, capacity + 1): # 1 to capacity
                dp[i][c] = max(profit[i] + dp[i][c - weight[i]], 
                dp[i + 1][c]) if weight[i] <= c else dp[i + 1][c]
        
        return dp[0][capacity]