class Solution:
    def maximumProfit2(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(weight)
        cache = dict()
        
        def dfs(i, capacity):
            if i >= n:
                return 0
            if capacity == 0:
                return 0
            
            if (i, capacity) in cache:
                return dfs[(i, capacity)]

            res = 0

            if weight[i] <= capacity:
                res = max(profit[i] + dfs(i + 1, capacity - weight[i]), dfs(i + 1, capacity))
            else:
                res = dfs(i + 1, capacity)
            
            return res

        return dfs(0, capacity)

    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(weight)

        dp = [[0] * (capacity + 1) for _ in range(n + 1)]

        for j in range(capacity + 1):
            dp[n][j] = 0
        
        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(n-1, -1, -1): # n-1 to 0
            for j in range(1, capacity + 1): # 1 to capacity
                dp[i][j] = max(profit[i] + dp[i + 1][j - weight[i]], dp[i + 1][j]) if weight[i] <= j else dp[i + 1][j]
        return dp[0][capacity]